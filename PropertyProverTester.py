

from t_core.messages import Packet
from t_core.iterator import Iterator
from t_core.matcher import Matcher
from t_core.rewriter import Rewriter


class PropertyProverTester:

    def set_artifacts(self, transformation, ruleTraceCheckers, matchRulePatterns, ruleCombinators):
        self.transformation = transformation
        self.rules = {}
        for layer in transformation:
            for rule in layer:
                self.rules[rule.name] = rule

        self.ruleTraceCheckers = ruleTraceCheckers
        self.matchRulePatterns = matchRulePatterns
        self.ruleCombinators = ruleCombinators

    def test_matchers(self):

        for rule_name in self.rules.keys():
            print("Testing matcher for " + rule_name)

            p = Packet()
            p.graph = self.rules[rule_name]

            matcher = self.matchRulePatterns[rule_name][0]

            matcher.packet_in(p)

            if not matcher.is_success:
                print("The matcher for " + rule_name + " did not match the rule")
            #    raise Exception("The matcher for " + rule_name + " did not match the rule")