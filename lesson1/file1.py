with open('referat.txt', 'r', encoding='utf-8') as referat:
    ref_text = referat.read()
    print(ref_text)
    print(f"Текст содержит {len(ref_text)} символов.")
    ref_words = ref_text.split(' ')
    print(f"В этом тексте содержится {len(ref_words)} слов.")
    print(f"В этом тексте {ref_text.count('.')} точек. И {ref_text.count('!')} восклицательных знаков.")
    ref_new_text = ref_text.replace('.', '!')
    print(f"После замены стало {ref_new_text.count('.')} точек. И {ref_new_text.count('!')} восклицательных знаков.")
    print(ref_words[7])
with open('referat2.txt', 'w', encoding='utf-8') as referat:
    referat.write(ref_new_text)