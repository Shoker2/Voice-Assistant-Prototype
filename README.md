gateway-server repository: https://github.com/biodora/voice-control-unit/tree/actual

## Оглавление
- [main](#main)
- [text2speach-server](#text2speach-server)


## main
В папке "main" лежит сам голосовой ассистент. "app.py" - это главный файл, также есть 2 доп.

"recognizer.py":
1) Перевод аудио в текст (возвращяет текст)
2) Нахождение цифр в тексте (цифры словами) и возвращяет float
3) Нахождение нужных слов в тексте из списка этих слов. Возврящет либо список слов или 1 слово с наибольшим процентом совпадения

"audio_io.py" - для работы с микрофоном (для получения аудио с микрофона)

## text2speach-server
В папке "text2speach-server" лежит сервер для озвучки текста.
