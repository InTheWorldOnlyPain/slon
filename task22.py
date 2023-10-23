import collections

text = 'Полгода назад произошел «Скачок», после этого во вселенную вернулась половина населения. Периодически власти США нанимают Сокола для выполнения ответственных заданий. Он часто бывает в командировках, одевая старый костюм. Соколу непонятно, как использовать щит, который ему передал Капитан Америка. Он не хочет брать на себя высокую ответственность. Из-за неуверенности в собственных силах Сокол решил, что щиту место в музее, посвященном Стиву Роджерсу.'
words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]

longest = max(words, key=len)

print(most_common, longest)