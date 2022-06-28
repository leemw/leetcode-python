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
    def _majorityElement(self, nums: List[int]) -> int:
        """ Brute force """
        element_count = {}
        majority_count = 0
        majority_number = None
        for element in nums:
            if element not in element_count:
                element_count[element] = 1
            else:
                element_count[element] += 1
            if element_count[element] > majority_count:
                majority_number = element
                majority_count = element_count[element]
        return majority_number

    def _majorityElement(self, nums: List[int]) -> int:
        """ Try with O(1) space """
        nums.sort()
        majority_count = 0
        majority_number = nums[0]
        current_count = 0
        last_element = nums[0]
        for element in nums:
            log.info("element: %s, last_element: %s, current_count: %s, majority_count: %s", element, last_element, current_count, majority_count)
            if element == last_element:
                current_count += 1
            else:
                if current_count >= majority_count:
                    log.info("l: assign element %s to majority number with count: %s", element, current_count + 1)
                    majority_count = current_count + 1
                    majority_number = last_element
                current_count = 0
            last_element = element
        current_count += 1
        log.info("element: %s, last_element: %s, current_count: %s, majority_count: %s", element, last_element, current_count, majority_count)

        if current_count >= majority_count:
            log.info("f: assign element %s to majority number with count: %s", element, current_count + 1)
            return element
        return majority_number

    def majorityElement(self, nums):
        """ Solution from disscussion """
        count = 0
        candidate = None

        for num in nums:
            log.info("num: %s, candidate: %s, count: %s", num, candidate, count)
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count += -1

        return candidate

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
        result = case_output["result"]
        # --------------------------------------------- #

        start_time = time.time()
        log.info("input: %s", case_input)
        log.info("result: %s", result)

        #
        # XXX: Change the function with parameters here
        #
        answer = Solution().majorityElement(nums)
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