import streamlit as st

st.title('Mythbusting the Job Search Pessimism')

st.markdown("""
#### By Salman Gassem
Ever since sophomore year in University, I’ve been wondering about my next step after I graduate. One thing that stood out for me is how little people talk about where to go for the best job opportunities, and all I heard was how hard it is to get a job.

I have always thought something was off, and not until I saw this dataset that all my doubts were confirmed.

The data I’m about to show you is from Jadarat, a Unified National Employment Platform for the Saudi people to find jobs.

I noticed that the place with the most job opportunities is Riyadh:
            """)
            
st.image('/Usecase-5/blob/main/images/Region_distribution.png', caption='', use_column_width=True)

st.markdown("""
The eastern and the western regions also offer great opportunities to get hired.

It’s expected for fresh grads to get no more than 18000 SR Salary.
            """)

st.image('images\salary_range.png', caption='', use_column_width=True)

st.markdown("""
Another point that I always disliked about spreading misinformation in this topic is that if you had no prior experience, you won't get hired. The graph below contradicts this statement in a big way:
""")

st.image('images\opportunities.png', caption='', use_column_width=True)

st.markdown("""
Most of the offerings are asking for fresh graduates, people with 0 years of experience! Such an uplifting view makes me optimistic for the future.

It’s also worth mentioning a fact that I am proud of, Saudi Arabia is rapidly evolving, and what drove this positive change are women. Although the chart below will show you a minor preference towards males, the percentages are almost equal, indicating that both genders are highly active in driving Saudi Arabia to heights never been reached before.
""")

st.image('images\gender_distribution.png', caption='', use_column_width=True)

st.markdown("""
So rest assured that as long as you work hard, and are actively searching, you will for sure find a job.

**Don’t let the muggles get you down!!**
""")
