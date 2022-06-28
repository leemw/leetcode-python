import logging
import time
from collections import deque
from typing import List

log = logging.getLogger(__name__)

log_level = "INFO"
logging.basicConfig(
    level=logging.getLevelName(log_level),
    format="%(asctime)s.%(msecs)03d - %(levelname)s - %(module)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.content = {}
        self.used_key = deque()

    def update_used_key(self, key):
        if key in self.used_key:

            self.used_key.pop(self.used_key.index(key))
        self.used_key.append(key)
        if len(self.used_key) == self.capacity + 1:
            self.used_key.pop(0)

    def get(self, key: int) -> int:
        if key in self.content:
            self.used_key.append(key)
            self.update_used_key(key)
            return self.content[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.content[key] = value

        if len(self.content) == self.capacity + 1:
            evict_k = self.used_key[0]
            del self.content[evict_k]

        self.update_used_key(key)

class _LRUCache:
    """ Use a list to maintain lease used key """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.content = {}
        self.used_key = []

    def update_used_key(self, key):
        if key in self.used_key:
            self.used_key.pop(self.used_key.index(key))
        self.used_key.append(key)
        if len(self.used_key) == self.capacity + 1:
            self.used_key.pop(0)

    def get(self, key: int) -> int:
        if key in self.content:
            self.update_used_key(key)
            return self.content[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.content[key] = value

        if len(self.content) == self.capacity + 1:
            evict_k = self.used_key[0]
            del self.content[evict_k]

        self.update_used_key(key)

class _LRUCache:
    """ Maintain least used by dictionary's order """
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.content = {}

    def update_content(self, key, value):
        if key in self.content:
            del self.content[key]
        self.content[key] = value
        if len(self.content) == self.capacity + 1:
            first_key = list(self.content.keys())[0]
            del self.content[first_key]

    def get(self, key: int) -> int:
        if key in self.content:
            value = self.content[key]
            self.update_content(key, value)
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.update_content(key, value)


if __name__ == "__main__":
    import os
    import sys
    curr_file_path = os.path.abspath(__file__)
    utils_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(curr_file_path)))

    sys.path.append(utils_dir)
    import argparse

    from utils.config import ConfigUtils

    case_path = ""
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", help="case file path",
                        default=case_path)
    args = parser.parse_args()
    case_path = args.case

    case_config = ConfigUtils().parse_config(case_path)

    case_cnt = 1
    wrong_index_list = []
    for case in case_config["Cases"]:
        log.info("cases number #%i", case_cnt)
        # XXX: Read input/output from yaml file
        case_input = case["Input"]
        case_output = case["Output"]

        #
        # XXX: Change the input parameters here
        #
        actions = case_input["actions"]
        action_value = case_input["action_value"]
        result = case_output["result"]
        # --------------------------------------------- #

        start_time = time.time()
        log.info("input: %s", case_input)
        log.info("result: %s", result)

        answer = [None]
        capacity = action_value[0][0]
        lru_cache = LRUCache(capacity=capacity)
        for i in range(1, len(actions)):
            func = actions[i]
            func_value = action_value[i]
            log.info("Step: %s, func: %s, func_value: %s", i, func.upper(), tuple(func_value))
            if func == "put":
                ret = lru_cache.put(key=func_value[0], value=func_value[1])
                answer.append(ret)
            elif func == "get":
                ret = lru_cache.get(key=func_value[0])
                answer.append(ret)
            else:
                raise Exception
            log.info("content: %s", lru_cache.content)
            log.info("---------------------")

        #
        # XXX: Change the function with parameters here
        #
        # answer = Solution().leetCodeTemplate(inputarg1)
        # --------------------------------------------- #

        end_time = time.time()
        log.info("function answer: %s", answer)
        if answer == result:
            log.info("Result correct")
        else:
            log.info("Result incorrect")
            wrong_index_list.append(case_cnt)

        case_cnt += 1
        log.info("Spend time: %f", end_time - start_time)
        log.info("--------------------------")
        # input("-------------- Enter to continue --------------")

    FinalResult = not bool(wrong_index_list)
    log.info("Code correct: %r", FinalResult)
    if not FinalResult:
        log.info("Wrong case index: %s", wrong_index_list)
