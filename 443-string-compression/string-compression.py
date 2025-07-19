class Solution(object):
    def compress(self, chars):
        temp = []
        read = 0
        while read < len(chars):
            current_char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == current_char:
                count += 1
                read += 1

            temp.append(current_char)
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    temp.append(digit)
            
        for i in range(len(temp)):
                chars[i] = temp[i]
                
        return len(temp)