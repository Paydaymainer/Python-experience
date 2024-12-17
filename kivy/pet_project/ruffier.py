''' Модуль для расчета результатов пробы Руфье.

Сумма измерений пульса в трех попытках (до нагрузки, сразу после и после короткого отдыха)
в идеале должна быть не более 200 ударов в минуту. 
Мы предлагаем детям измерять свой пульс на протяжении 15 секунд, 
и приводим результат к ударам в минуту умножением на 4:
    S = 4 * (P1 + P2 + P3)
Чем дальше этот результат от идеальных 200 ударов, тем хуже.
Традиционно таблицы даются для величины, делённой на 10. 

Индекс Руфье   
    IR = (S - 200) / 10
оценивается по таблице в соответствии с возрастом:
        7-8             9-10                11-12               13-14               15+ (только для подростков!)
отл.     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
хор.    >= 6.5 и < 12   >= 5 и < 10.5       >= 3.5 и < 9        >= 2 и < 7.5        >= 0.5 и < 6
удовл.  >= 12 и < 17    >= 10.5 и < 15.5    >= 9 и < 14         >= 7.5 и < 12.5     >= 6 и < 11
слабый  >= 17 и < 21    >= 15.5 и < 19.5    >= 14 и < 18        >= 12.5 и < 16.5    >= 11 и < 15
неуд.   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

для всех возрастов результат "неуд" отстоит от "слабого" на 4, 
тот от "удовлетворительного" на 5, а "хороший" от "уд" - на 5.5

поэтому напишем функцию ruffier_result(r_index, level), которая будет получать
рассчитанный индекс Руфье и уровень "неуд" для возраста тестируемого, и отдавать результат

'''
txt_index = "Your Ruffier index: "
txt_workheart = "Heart's effectiveness: "
txt_nodata = '''no data for this age'''
txt_res = [] 
txt_res.append('''low. 
    Urgently consult a doctor!''')
txt_res.append('''enough. 
    Please consult a doctor!''')
txt_res.append('''normal. 
    Maybe, it is recommended to do additional check up.''')

txt_res.append('''
    more than normal''')
txt_res.append('''
    high''')

def ruffier_index(P1, P2, P3):
    ''' returns the index value for three heart rate indicators for comparison with the table'''
    return (4 * (P1+P2+P3) - 200) / 10

def neud_level(age):
    ''' variants with an age less than 7 and adults must be processed separately, 
    here we select the “failure” level only inside the table:
    at the age of 7 years, “failure” is an index of 21, then every 2 years it decreases by 1.5 to a value of 15 at 15-16 years '''
    norm_age = (min(age, 15) - 7) // 2  
    result = 21 - norm_age * 1.5 
    return result 
    
def ruffier_result(r_index, level):
    ''' the function receives the Ruffier index and interprets it, 
    returns readiness level: a number from 0 to 4
    (the higher the level of readiness, the better).  '''
    if r_index >= level:
        return 0
    level = level - 4 
    if r_index >= level:
        return 1
    level = level - 5 
    if r_index >= level:
        return 2
    level = level - 5.5 
    if r_index >= level:
        return 3
    return 4 

def test(P1, P2, P3, age):
    ''' this function can be used outside the module to calculate the Ruffier index.
    Returns ready-made texts that just need to be drawn in the right place
    Uses the constants specified at the beginning of this module for texts. '''
    if age < 7:
        return (txt_index + "0", txt_nodata) 
    else:
        r_index = ruffier_index(P1, P2, P3) 
        result = txt_res[ruffier_result(r_index, neud_level(age))] 
        return (txt_index + str(r_index), txt_workheart + result) 