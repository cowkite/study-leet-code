class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_numbers = version1.split('.')
        v2_numbers = version2.split('.')

        compareable_unit = min(len(v1_numbers), len(v2_numbers))
        for i in range(compareable_unit):
            if int(v1_numbers[i]) < int(v2_numbers[i]):
                return -1
            elif int(v1_numbers[i]) > int(v2_numbers[i]):
                return 1

        if len(v1_numbers) == len(v2_numbers):
            return 0

        v1_rest = "".join(v1_numbers[compareable_unit:])
        v2_rest = "".join(v2_numbers[compareable_unit:])

        v1_rest_int = int(v1_rest) if v1_rest else 0
        v2_rest_int = int(v2_rest) if v2_rest else 0

        return 1 if v1_rest_int > 0 else -1 if v2_rest_int > 0 else 0

        