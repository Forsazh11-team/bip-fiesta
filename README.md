# bip-fiesta

В main напрямую код не заливаем. Настроил правило для этого: только через MR, 2 одобрения нужно.

Алгоритм работы примерно такой:
- main содержит уже готовые рабочие части, которые можно показывать;
- в ветке dev происходит основная работа. Клонируете ветку dev -> создаете свою ветку на ее основе -> делаете фичу -> открываете MR в dev;
- периодически по готовности код из dev будет вливаться в main.

Dev пока не создал и никак не ограничивал, но пушить напрямую, наверное, тоже нехорошо туда. Посмотрим.
