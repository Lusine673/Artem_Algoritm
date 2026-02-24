import streamlit as st

# Настройка страницы
st.set_page_config(page_title="Алгоритм ЭД", layout="centered")

# --- Инициализация состояния (памяти приложения) ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'plan' not in st.session_state:
    st.session_state.plan = []

# Функция для перехода на следующий шаг
def next_step():
    st.session_state.step += 1

# Функция для сброса (начать заново)
def restart():
    st.session_state.step = 1
    st.session_state.plan = []

# Заголовок (всегда сверху, но компактный)
st.markdown("### Реабилитация пациента с ЭД")
# Прогресс-бар (визуально показывает, далеко ли до конца)
progress_value = (st.session_state.step - 1) / 5
st.progress(progress_value)

# --- ЛОГИКА ШАГОВ ---

# ШАГ 1: Санация
if st.session_state.step == 1:
    st.info("Этап 1: Хирургическая санация")
    st.write("Необходимо удаление временных и нежизнеспособных зубов.")
    
    # Кнопка одна - подтверждение прохождения этапа
    if st.button("Этап пройден / Далее", type="primary", use_container_width=True):
        st.session_state.plan.append("1. Хирургическая санация выполнена.")
        next_step()
        st.rerun()

# ШАГ 2: Костная пластика
elif st.session_state.step == 2:
    st.info("Этап 2: Костная пластика")
    st.write("Реконструктивная операция (теменные аутотрансплантаты / синуслифтинг).")
    
    if st.button("Этап пройден / Далее", type="primary", use_container_width=True):
        st.session_state.plan.append("2. Реконструктивная костно-пластическая операция выполнена.")
        next_step()
        st.rerun()

# ШАГ 3: Имплантация
elif st.session_state.step == 3:
    st.info("Этап 3: Дентальная имплантация")
    st.write("Установка имплантатов.")
    
    if st.button("Этап пройден / Далее", type="primary", use_container_width=True):
        st.session_state.plan.append("3. Дентальная имплантация выполнена.")
        next_step()
        st.rerun()

# ШАГ 4: Вопрос про металл (Ветвление 1)
elif st.session_state.step == 4:
    st.warning("Диагностика мягких тканей")
    st.write("Наблюдается ли **просвечивание металла** через слизистую?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Да (Дефицит)", type="primary", use_container_width=True):
            st.session_state.plan.append("4. **Требуется:** Установка формирователей десны с коррекцией мягких тканей.")
            next_step()
            st.rerun()
            
    with col2:
        if st.button("Нет (Норма)", use_container_width=True):
            st.session_state.plan.append("4. Коррекция мягких тканей не требуется.")
            next_step()
            st.rerun()

# ШАГ 5: Вопрос про челюсть (Ветвление 2)
elif st.session_state.step == 5:
    st.warning("Оценка прикуса")
    st.write("Имеется ли сочетанная деформация челюстей (мезиальная окклюзия, III класс)?")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Да (Деформация)", type="primary", use_container_width=True):
            st.session_state.plan.append("5. **Требуется:** Ортогнатическая операция.")
            next_step()
            st.rerun()
            
    with col2:
        if st.button("Нет (Норма)", use_container_width=True):
            st.session_state.plan.append("5. Ортогнатическая операция не требуется.")
            next_step()
            st.rerun()

# ФИНАЛ: Результат
elif st.session_state.step > 5:
    st.success("✅ План лечения сформирован")
    
    # Добавляем финальный обязательный пункт
    st.session_state.plan.append("6. Изготовление и установка ортопедической конструкции.")
    
    # Выводим красивый список только уникальных записей (на всякий случай)
    final_plan_display = list(dict.fromkeys(st.session_state.plan))
    
    for item in final_plan_display:
        st.write(item)
    
    st.markdown("---")
    if st.button("Начать заново с новым пациентом", type="secondary", use_container_width=True):
        restart()
        st.rerun()
