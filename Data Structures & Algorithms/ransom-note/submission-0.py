class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counterRans =Counter(ransomNote)
        counterMagazine =Counter(magazine)

        for ch in ransomNote:
            if counterRans[ch]>counterMagazine[ch]:
                return False

        
        return True
