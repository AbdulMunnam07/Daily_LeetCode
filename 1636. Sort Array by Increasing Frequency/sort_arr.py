class Solution:
	def frequencySort(self, nums: List[int]) -> List[int]:
		d = Counter(nums)
		def check(x):
			return d[x]

		nums.sort(reverse=True)
		nums.sort(key=check)
		return nums