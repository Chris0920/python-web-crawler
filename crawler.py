
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None, 0
    else:
    #Insert your code below here
    
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote

def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''

def print_all_links(page):
	while True:
		url, endpos = get_next_target(page)
		if url:
			print url
			page = page[endpos:]
		else:
			break

print_all_links(get_page('http://xkcd.com/353'))

# def factorial(n):
#       if n <= 1:
#             return 1
#       else:
#             return n*factorial(n-1)

# def factorial(n):
# 	while n >= 1:
# 		i = n * (n-1)
# 		n * i


# def factorial(n):
# 	i = n
# 	while i >= 1:
# 		i = i - 1
# 		n * i 
# 		return n

# def factorialc(n):
# 	if n == 0:
# 		return 1
# 	else:
# 		result = n
# 		while n > 1:
# 			n = n - 1
# 			result = result*n
# 		return result

# def factorialk(n):
# 	result = n
# 	while n > 1:
# 		n = n - 1
# 		result = result*n
# 	return result


# print factorialc(6)
# print factorialk(6)

# result = n * (n-1)

# def sum(a,b):
# 	a = a + b
# 	return a 

# def square(num):
# 	num = num * num
# 	return num


# print sum(2, 4)

# print square(5)
                  
# def print_numbers(num):
# 		i = 0
#     while i > num:
#     	i = i + 1
#     	print i

# print print_numbers(8)


# def print_numbers(num):
# 	i = 0
# 	while i < num:
# 		i = i + 1
# 		print i

# print_numbers(5)