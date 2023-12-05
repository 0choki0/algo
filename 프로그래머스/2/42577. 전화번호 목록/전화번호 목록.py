def solution(phone_book):
    book = {}
    for number in phone_book:
        book[number] = 1

    for number in phone_book:
        num = ''
        for i in number:
            num += i
            if num in book and num != number:
                return False
    
    return True