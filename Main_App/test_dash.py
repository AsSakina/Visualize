with col2:
        st.header('Global Distribution of Mental Health Disorders')
        choropleth = make_choropleth(data, selected_year, selected_disorder, selected_color_theme)
        st.plotly_chart(choropleth)