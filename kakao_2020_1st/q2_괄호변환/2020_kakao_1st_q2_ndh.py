def solution(s):

    # 배열 크기를 받는 문자열 크기로 정의하지 않을 시
    # 테스트 5번 런타임 에러남.
    answer = [len(s)]

    for i in range(1, len(s)):
        # range(a,b,c) 에서의 c 의미
        # for문을 i크기 만큼 증가시킨다.
        temp = [s[k:k+i] for k in range(0, len(s), i)]

        result = ""
        count = 1

    # n글자씩 비교시 같으면 count++, 다르면 nx로 문자열 추가삽입
        for j in range(1, len(temp)):
            prev, curr = temp[j-1], temp[j]
            if prev == curr:
                count += 1
            else:
                if count > 1:
                    result += str(count)
                result += prev
                count = 1

    # 마지막 위치의 배열값 구분 처리
    # 위 j for문 기준이 끝에서 -1번째(prev)기 때문에, 마지막 문자열에 대한 처리를 따로 해주어야함
        if count > 1:
            result += str(count)
        result += temp[-1]
    # 경우의 수 별 문자열 길이를 answer 배열에 삽입
    # 경우의 수가 문자열 길이를 넘지 않기 때문에 위에서 anser = [len(s)] 처리하면 됨
        answer.append(len(result))

    # 최소 값이 정답
    return min(answer)
