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
                    {"QUEUE_TAG": random_string(), "ENTRY_POINT_ID": random.randint(1, 99999),
                     "CHAT_TITLE": random_string(), "LANGUAGE": random.choice["ru", "ua", "en"],
                     "COUNTRY": random.choice['Ukraine', 'Russia', "England"], "VERSION": random.randint(1, 99999)}]
        not_required = [{"RECORD_CONVERSATIONS": random.choice([True, False])},
                        {"SHOW_PREVIOUS_N_DIALOGS": random.randint(1, 100)}]
        return required + random.sample(not_required, k=1)

    @staticmethod
    def bot():
        required = [{"SCRIPT_ID": random.randint(1, 9999)}, {"AS_URL": "http://" + random_string()},
                    {"DEFAULT_SESSION_TIMEOUT": random.randint(1, 9999)}]
        not_required = [{"RECORD_CONVERSATIONS": random.choice([True, False])},
                        {"DEFAULT_ACCOUNT_ID": random.randint(1, 100)}]
        return required + random.sample(not_required, k=1)


# [{"name":"CONNECTOR_URL","value":""},{"name":"RECORD_CONVERSATIONS","value":"false"},{"name":"AUTH_TOKEN","value":"********"}]


print(Property.social_miner())
