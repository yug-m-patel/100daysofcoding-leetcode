class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1=nums1+nums2
        nums1.sort()
        n=len(nums1)
        if n%2==0:
            return (float)(nums1[(n/2)-1]+nums1[(n/2)])/2
        else:
            return nums1[n/2]
