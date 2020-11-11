from collections import defaultdict 

MAX_CHARS = 100001

def LenString(string): 
	
	n = len(string) 
	
	dist_count = len(set([x for x in string])) 
	
	curr_count = defaultdict(lambda: 0) 
	count = 0
	start = 0
	start_index = 0
	min_len = n 
	
	for j in range(n): 
		curr_count[string[j]] += 1
		

		if curr_count[string[j]] == 1: 
			count += 1
			
		if count == dist_count: 
			while curr_count[string[start]] > 1: 
				if curr_count[string[start]] > 1: 
					curr_count[string[start]] -= 1
					
				start += 1
				
			len_window = j - start + 1
			
			if min_len > len_window: 
				min_len = len_window 
				start_index = start 
	return len(str(string[start_index: start_index + min_len]))
								
# Driver code 
if __name__=='__main__': 
	print(LenString(input()))