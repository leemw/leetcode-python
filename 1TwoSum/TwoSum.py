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
    def _twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)

        for i in range(l):
            curr_val = nums[i]
            nums[i] = None
            if target-curr_val in nums:
                return [i, nums.index(target-curr_val)]

        return [-1, -1]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for i in range(len(nums)):
            curr_val = nums[i]
            if target-curr_val in d:
                return [i, d[target-curr_val]]
            else:
                d[curr_val] = i

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
        nums = case_input["nums"]
        target = case_input["target"]
        result = case_output["result"]
        # --------------------------------------------- #

        start_time = time.time()
        log.info("input: %s", case_input)
        log.info("result: %s", result)

        #
        # XXX: Change the function with parameters here
        #
        answer = Solution().twoSum(nums, target)
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