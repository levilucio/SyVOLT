

from t_core.messages import Packet
from t_core.iterator import Iterator
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter

from core.himesis_utils import graph_to_dot

import time

class Tester:

    def __init__(self, args):
        self.draw_svg = args.draw_svg
        self.draw_rules = args.draw_rules

        self.run_tests = args.run_tests

        self.transformation = None
        self.rules = None
        self.ruleTraceCheckers = None
        self.matchRulePatterns = None
        self.ruleCombinators = None
        self.rule_names = None


    def debug(self):
        if self.draw_svg or self.draw_rules:
            print("Drawing svgs...")
            self.print_transformation()

        if self.draw_svg:
            self.print_ruleCombinators()
            self.print_ruleTraceCheckers()
            self.print_matchRulePatterns()

        if self.run_tests:
            self.test_matchRulePatterns()
            self.test_ruleTraceCheckers()
            self.test_ruleCombinators()

        #
        self.transformation = None
        self.rules = None
        self.ruleTraceCheckers = None
        self.matchRulePatterns = None
        self.ruleCombinators = None
        self.rule_names = None

    def set_artifacts(self, transformation, ruleTraceCheckers, matchRulePatterns, ruleCombinators, rule_names):
        self.transformation = transformation
        self.rules = {}
        for layer in transformation:
            for rule in layer:
                self.rules[rule.name] = rule

        self.ruleTraceCheckers = ruleTraceCheckers
        self.matchRulePatterns = matchRulePatterns
        self.ruleCombinators = ruleCombinators
        self.rule_names = rule_names

    def print_transformation(self):
        for layer in self.transformation:
            for rule in layer:
                graph_to_dot("rule_" + str(self.rule_names[rule.name]), rule)

    def print_ruleCombinators(self):
        for key in self.rules:

            if not self.ruleCombinators[key]:
                continue

            value = self.ruleCombinators[key]
            for (m, r) in value:
                graph_to_dot("ruleCombinator_match_" + str(m.condition.name), m.condition)
                graph_to_dot("ruleCombinator_rewrite_" + str(r.condition.name), r.condition)

                if len(m.condition.NACs) > 0:
                    graph_to_dot("ruleCombinator_NAC_" + str(m.condition.name), m.condition.NACs[0])


    def print_ruleTraceCheckers(self):
        for key in self.rules:
            if self.ruleTraceCheckers[key] is None:
                continue

            tc = self.ruleTraceCheckers[key]
            graph_to_dot("traceChecker_" + str(tc.condition.name), tc.condition)

    def print_matchRulePatterns(self):
        for key in self.rules:
            if self.matchRulePatterns[key] is None:
                continue

            matcher, rewriter = self.matchRulePatterns[key]
            graph_to_dot("matchPattern_matcher_" + str(matcher.condition.name), matcher.condition)
            graph_to_dot("matchPattern_rewriter_" + str(rewriter.condition.name), rewriter.condition)


    def test_matchRulePatterns(self):

        for rule_name in sorted(self.rules.keys()):
            #print("Testing match rule pattern for " + self.rule_names[rule_name])

            p = Packet()
            p.graph = self.rules[rule_name].copy()

            matcher = self.matchRulePatterns[rule_name][0]

            matcher.packet_in(p)

            if not matcher.is_success:
                raise Exception("The matcher for " + self.rule_names[rule_name] + " did not match the rule")

            rewriter = self.matchRulePatterns[rule_name][0]
            rewriter.packet_in(p)

            if not rewriter.is_success:
                raise Exception("The rewriter for " + self.rule_names[rule_name] + " did not rewrite successfully")

    def test_ruleTraceCheckers(self):

        for rule_name in sorted(self.rules.keys()):

            if not rule_name in self.ruleTraceCheckers.keys():
                continue

            #print("Testing rule trace checkers for " + self.rule_names[rule_name])

            p = Packet()
            p.graph = self.rules[rule_name]

            matcher = self.ruleTraceCheckers[rule_name]

            if matcher is None:
                continue

            matcher.packet_in(p)

            if not matcher.is_success:
                raise Exception("The matcher for " + self.rule_names[rule_name] + " did not match the rule")

    def test_ruleCombinators(self):
        for rule_name in sorted(self.rules.keys()):
            #print("Testing rule combinators for " + self.rule_names[rule_name])

            if self.ruleCombinators[rule_name] is None:
                continue

            #get the last matcher/rewriter combo
            #which should be the total matcher
            rc = self.ruleCombinators[rule_name][-1]

            p = Packet()
            p.graph = self.rules[rule_name].copy()

            matcher = rc[0]
            matcher.packet_in(p)

            if not matcher.is_success:
                raise Exception("The matcher for " + self.rule_names[rule_name] + " did not match the rule")

            rewriter = rc[1]

            i = Iterator()
            p = i.packet_in(p)

            rewriter.packet_in(p)

            if not rewriter.is_success:
                raise Exception("The rewriter for " + self.rule_names[rule_name] + " did not rewrite successfully")


    def check_rule_reachability(self, pathCondGen, curr_layer):

        #reachability_start = time.time()
        #see if any rules are missing
        rules = []
        for i, layer in enumerate(pathCondGen.transformation):
            if i > curr_layer:
                break

            for rule in layer:
                real_name = pathCondGen.rule_names[rule.name]
                rules.append(real_name)

        rules_seen = []
        for pc, pc_name in pathCondGen.get_path_conditions(expand = False):
            rules_in_pc = pathCondGen.rules_in_pc_name(pc_name)
            #print(rules_in_pc)
            rules_seen += rules_in_pc

        rules_seen = set(rules_seen)
        rules_not_seen = []
        #print("Rules seen: " + str(rules_seen))
        for rule in rules:
            if rule not in rules_seen:
                print("ERROR: Rule " + rule + " was not executed!")
                print("Rules seen:")
                print(rules_seen)
                rules_not_seen.append(rule)

        #print("Reachability check took " + str(time.time() - reachability_start) + " seconds")

        if len(rules_not_seen) > 0:
           raise Exception()

