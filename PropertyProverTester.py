

from t_core.messages import Packet
from t_core.iterator import Iterator
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter

from core.himesis_plus import *

class PropertyProverTester:

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

    def test_matchRulePatterns(self):

        for rule_name in sorted(self.rules.keys()):
            print("Testing match rule pattern for " + self.rule_names[rule_name])

            p = Packet()
            p.graph = copy_graph(self.rules[rule_name])

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

            print("Testing rule trace checkers for " + self.rule_names[rule_name])

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
            print("Testing rule combinators for " + self.rule_names[rule_name])

            if self.ruleCombinators[rule_name] is None:
                continue

            #get the last matcher/rewriter combo
            #which should be the total matcher
            rc = self.ruleCombinators[rule_name][-1]

            p = Packet()
            p.graph = copy_graph(self.rules[rule_name])

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




