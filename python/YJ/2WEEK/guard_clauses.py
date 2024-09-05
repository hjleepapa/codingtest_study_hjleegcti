# 보호 구문, 앞쪽에서 예외처리 후 뒤에서 본 로직

def calc_avg(numbers):
    # 값이 없는 경우 종료
    if numbers is None:
        return None
    # numbers 자료형이 리스트가 아니라면 종료
    if not isinstance(numbers, list):
        return None
    # numbers 에 데이터가 없다면 종료
    if len(numbers) == 0:
        return None
    
    total = sum(numbers)
    avg = total / len(numbers)
    return avg