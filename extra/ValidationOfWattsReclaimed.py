# Estimation and Validation of Watts lost and Watts reclaimed from Heat Acclimatisation.


# I asked Gemini to convert Figure 1 of  <a href="https://www.researchgate.net/publication/263514484_Effect_of_Heat_and_Heat_Acclimatization_on_Cycling_Time_Trial_Performance_and_Pacing"> Racinais (2015)</a> into a table and regenerate approximately the same chart.
# I calculated average power and confirmed that there was a 15.9% loss of power for TTH1 versus TCC compared with 16% quoted in the text
# I calculated average power for TTH2 and TTH3 in order to calibrate the Simulation in the main app. 
# Although more of the watts are regained in the first 7 days, I had to apply quite a high weight to the Heat Stress Proteins

    # 3. Mitigation Weightings (Contribution to total performance recovery)
#    w_cv = (plasma_vol_pct / 15.0) * 0.35          # 35% CV stability
#    w_thermal = (abs(poah_shift_c) / 0.45) * 0.30  # 30% Thermoregulatory offset
#    w_cellular = ((hsp_fold_change - 1.0) / 2.5) * 0.35 # 35% Cellular protection

import plotly.graph_objects as go
from plotly.subplots import make_subplots

def testplot():
    # Data from the table
    x_axis = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    tcc = [322, 318, 309, 301, 298, 298, 299, 299, 300, 302]
    tth3 = [319, 312, 298, 294, 294, 285, 284, 282, 280, 289]
    tth2 = [316, 305, 288, 285, 276, 261, 268, 270, 259, 268]
    tth1 = [315, 298, 273, 270, 248, 242, 239, 226, 225, 226]

    # Set up the plot
    fig = go.Figure()

    # Plot each line with its corresponding style
    fig.add_trace(go.Scatter(
        x=x_axis, y=tcc, name='TCC', mode='lines',
        line=dict(color='black', width=2, dash='solid')
    ))
    fig.add_trace(go.Scatter(
        x=x_axis, y=tth3, name='TTH-3', mode='lines',
        line=dict(color='black', width=2, dash='dot')
    ))
    fig.add_trace(go.Scatter(
        x=x_axis, y=tth2, name='TTH-2', mode='lines',
        line=dict(color='black', width=2, dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=x_axis, y=tth1, name='TTH-1', mode='lines',
        line=dict(color='black', width=2, dash='10px,5px') # Custom dash matching Matplotlib
    ))

    # Format the axes, labels, and layout
    fig.update_layout(
        xaxis_title='X-Axis',
        yaxis_title='Power (W)',
        xaxis=dict(tickmode='array', tickvals=x_axis, range=[5, 105]),
        yaxis=dict(range=[180, 330]),
        template='simple_white',  # Provides a clean, white background
        legend=dict(yanchor="middle", y=0.5, xanchor="left", x=1.05) # Moves legend outside the plot
    )

    # Display the chart
    fig.show()
    print([sum(i)/10-sum(tth1)/10 for i in [tcc,tth1,tth2,tth3]])
    print([(sum(i)/sum(tcc)-1,(sum(i)/sum(tcc)-1)/(sum(tth1)/sum(tcc)-1)-1) for i in [tth1,tth2,tth3]])

testplot()