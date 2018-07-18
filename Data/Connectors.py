import random
from bin.common import random_string


class Property:

    @staticmethod
    def social_miner():
        required = [{"CHAT_URL": random_string()}, {"CHAT_FORM_ID": random.randint(1, 99999)},
                    {"QUEUE_TAG": random_string()}]
        not_required = [{"RECORD_CONVERSATIONS": random.choice([True, False])},
                        {"SHOW_PREVIOUS_N_DIALOGS": random.randint(1, 100)}]
        return required + random.sample(not_required, k=1)

    @staticmethod
    def ECE():
        required = [{"CHAT_URL": random_string()}, {"CHAT_FORM_ID": random.randint(1, 99999)},
                    {"QUEUE_TAG": random_string()}]
        not_required = [{"RECORD_CONVERSATIONS": random.choice([True, False])},
                        {"SHOW_PREVIOUS_N_DIALOGS": random.randint(1, 100)}]
        return required + random.sample(not_required, k=1)

# [{"name":"CONNECTOR_URL","value":""},{"name":"RECORD_CONVERSATIONS","value":"false"},{"name":"AUTH_TOKEN","value":"********"}]


print(Property.social_miner())