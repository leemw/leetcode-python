import logging
from typing import List
import time

log = logging.getLogger(__name__)

log_level = "INFO"
logging.basicConfig(
    level=logging.getLevelName(log_level),
    format="%(asctime)s.%(msecs)03d - %(levelname)s - %(module)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class Solution:
    def _groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        grp_dict = {}
        for word in strs:
            char_dict = {}
            for char in word:
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1

            key = ""
            for k in sorted(char_dict.keys()):
                v = char_dict[k]
                key += k + str(v)
            if key in grp_dict:
                grp_dict[key].append(word)
            else:
                grp_dict[key] = [word]
        return list(grp_dict.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Answer reivew from others at LeetCode discussion
        """

        grp_dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key in grp_dict:
                grp_dict[key].append(word)
            else:
                grp_dict[key] = [word]
        return list(grp_dict.values())



if __name__ == "__main__":
    import sys
    import os
    curr_file_path = os.path.abspath(__file__)
    utils_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(curr_file_path)))

    sys.path.append(utils_dir)
    from utils.config import ConfigUtils
    import argparse

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
        # TODO: Read input/output from yaml file
        case_input = case["Input"]
        case_output = case["Output"]

        #
        # XXX: Change the input parameters here
        #
        strs = case_input["strs"]
        result = case_output["result"]
        # --------------------------------------------- #

        start_time = time.time()
        log.info("input: %s", case_input)
        log.info("result: %s", result)

        #
        # XXX: Change the function with parameters here
        #
        answer = Solution().groupAnagrams(strs)
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