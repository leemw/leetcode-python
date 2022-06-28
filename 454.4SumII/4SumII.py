import logging
import time
from typing import List

log = logging.getLogger(__name__)

log_level = "INFO"
logging.basicConfig(
    level=logging.getLevelName(log_level),
    format="%(asctime)s.%(msecs)03d - %(levelname)s - %(module)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


class Solution:

    def get_sub_dict(self, n1, n2):
        n12 = {}
        total = 0
        for v1 in n1:
            total += v1
            for v2 in n2:
                total += v2
                if total in n12:
                    n12[total] += 1
                else:
                    n12[total] = 1
                total -= v2
            total -= v1
        return n12

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        n12 = self.get_sub_dict(nums1, nums2)
        n34 = self.get_sub_dict(nums3, nums4)
        log.info("n12: %s, n34: %s", n12, n34)
        answer = 0
        for i in n12:
            if -i in n34:
                answer += n12[i] * n34[-i]
        return answer


    def get_num_cnt_dict(self, nums):
        res = {}
        for k in nums:
            if k in res:
                res[k] += 1
            else:
                res[k] = 1
        return res

    def _fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        n1_dict = self.get_num_cnt_dict(nums1)
        n2_dict = self.get_num_cnt_dict(nums2)
        n3_dict = self.get_num_cnt_dict(nums3)
        n4_dict = self.get_num_cnt_dict(nums4)

        answer = 0
        total = 0
        for v1 in n1_dict.keys():
            total += v1
            for v2 in n2_dict.keys():
                total += v2
                for v3 in n3_dict.keys():
                    total += v3
                    if -total in n4_dict:
                        answer += n1_dict[v1] * n2_dict[v2] * n3_dict[v3] * n4_dict[-total]
                    total -= v3
                total -= v2
            total -= v1
        return answer


    def _fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        answer = 0
        total = 0
        answer_detail = []
        for i1, v1 in enumerate(nums1):
            total += v1
            for i2, v2 in enumerate(nums2):
                total += v2
                for i3, v3 in enumerate(nums3):
                    total += v3
                    log.info("Check for nums1[%d]: %d, nums2[%d]: %d, nums3[%d]: %d", i1, v1, i2, v2, i3, v3)
                    for i4, v4 in enumerate(nums4):
                        if -total == v4:
                            answer += 1
                            answer_detail.append([i1, i2, i3, nums4.index(-total)])
                    total -= v3
                total -= v2
            total -= v1

        log.info("answer_detail: %s", answer_detail)
        return answer


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
        # TODO: Read input/output from yaml file
        case_input = case["Input"]
        case_output = case["Output"]

        #
        # XXX: Change the input parameters here
        #
        nums1 = case_input["nums1"]
        nums2 = case_input["nums2"]
        nums3 = case_input["nums3"]
        nums4 = case_input["nums4"]
        result = case_output["result"]
        # --------------------------------------------- #

        start_time = time.time()
        log.info("input: %s", case_input)
        log.info("result: %s", result)

        #
        # XXX: Change the function with parameters here
        #
        answer = Solution().fourSumCount(nums1, nums2, nums3, nums4)
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
