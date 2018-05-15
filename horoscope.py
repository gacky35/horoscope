import random
import time

def max(vals):
    max = 0
    maxi = -1
    for i, x in enumerate(vals):
        if x > max:
            maxi = i
            max = x
    return maxi

def second(vals):
    first = vals[max(vals)]
    second = 0
    secondi = -1
    for i, x in enumerate(vals):
        if x < first and x > second:
            secondi = i
            second = x
    return secondi

def third(vals):
    sec = vals[second(vals)]
    third = 0
    thirdi = -1
    for i, x in enumerate(vals):
        if x < sec and x > third:
            thirdi = i
            third = x
    return thirdi

def main():
    constellation = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    colors = ["Red", "Blue", "Green", "Yellow", "White", "Black", "Purple", "Violet", "Indigo", "Sky", "Pink", "Ash", "Brown", "Orange", "Cyan"]
    cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cnt2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(0, 100000):
        cnt[random.randint(0, 11)] += 1
        cnt2[random.randint(0, 14)] += 1

    print("今日の運勢No.3は" + constellation[third(cnt)] + "だよ！")
    print("そしてラッキーカラーは" + colors[third(cnt2)] + "だよ！")
    time.sleep(2)
    print("今日の運勢No.2は" + constellation[second(cnt)] + "だよ！")
    print("そしてラッキーカラーは" + colors[second(cnt2)] + "だよ！")
    time.sleep(4)
    print("今日の運勢No.1は" + constellation[max(cnt)] + "だよ！")
    print("そしてラッキーカラーは" + colors[max(cnt2)] + "だよ！")


main()
