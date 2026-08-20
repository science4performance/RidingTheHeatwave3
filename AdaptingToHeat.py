# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "numpy==2.4.6",
#     "pandas==3.0.5",
#     "plotly==6.9.0",
# ]
# ///

import marimo

__generated_with = "0.18.3"
app = marimo.App(
    width="medium",
    app_title="Science4Performance | Heat Acclimation ROI Engine",
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Adapting to a Warmer World: The Physiological Adaptions of Heat Acclimation
    <blockquote cite="https://www.huxley.net/bnw/four.html">
        <p>
          Heat acclimation develops through frequent exposure to hot environmental conditions, which elicit responses that attenuate the negative effects of heat stress
        <cite><a href="https://www.researchgate.net/publication/275954405_Adaptations_and_mechanisms_of_human_heat_acclimation_Applications_for_competitive_athletes_and_sports">Périad (2015)</a></cite>
        </p>
        </blockquote>
    Having considered the physics of thermoregulation and the body's acute responses to heat, it is natural to ask how athletes can adapt to maintain performance in hot, humid conditions. If you use a Garmin device to track your training, you might have occasionally noticed messages indicating your level of heat (or altitude) acclimation. While acclimatisation refers to longer term adaptation to changes in environmental conditions, such as moving from Scotland to the south of Spain or an elevated alpine village, **acclimation** describes physiological changes occurring over 10 to 14 days, typically induced by artificial exercise conditions, such as indoor heat training or an altitude camp.<br>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Heat Training Protocol
    The paradox of heat training is that you start by removing your greatest cooling asset: airspeed. Even at relatively low power of around 150 W, pedalling on an indoor turbo-trainer in a warm room without a fan fairly quickly induces an increase in core body temperature. Professional athletes typically follow a protocol aiming to raise core body temperature to $38.5^\circ\text{C}\text{--}39.0^\circ\text{C}$ for 60 to 90 minutes a day. With the benefit of expert supervision, the target is to maintain a safe, elevated temperature. By carefulling controlling the ambient conditions and layers of clothing, athletes do not need to expend excessive energy generating high power.<br>
    During a 14-day heat acclimation block, physiological adaptations occur in sequence. The body prioritises fluid expansion to support cardiovascular blood flow. Then it recalibrates sweat regulation and the peripheral sweat response. The transformation is completed with cellular and metabolic reinforcement.
    ## Increased Plasma Volume (days 1 to 5)
    Repeated heat stress triggers mechanisms to retain water and reduce the loss of sodium. These include the release of aldosterone and ADH (vasopressin) to retain water and albumin to draw the water into the bloodstream. This results in a  5-7% increase in body water. Any disadvantages of higher body mass are outweighed by the benefits to thermoregulation and cardiovascular stability. Blood plasma levels rise by 4-15%, resulting in a temporary decrease in haematocrit (concentration of red blood cells). This contrasts with the effect of altitude acclimation.<br>
    The expansion of plasma volume alleviates the conflict of demand for blood to flow both to the muscles to do work and the skin for cooling. This helps stablise blood pressure and reduce the elevation of heart rate (cardiovascular drift).
    ## Recalibration of the Sweat Thermostat (days 4 to 6)
    The brain's thermostat resides in the Preoptic Anterior Hypothalamus (POAH). The threshold for the central control of the sweat response falls by 0.3°C to 0.5°C, early in acclimation. Your cooling response kicks in earlier by starting to sweat at a slightly lower temperature.
    ## Sweat Rate and Electrolyte Conservation (days 7 to 10)
    At the level of the skin, not only does the sweat response start earlier, it also becomes more sensitive, producing a greater volume of sweat. This allows the you to keep cooler in hot weather.<br>
    The sweat glands upregulate enzymes that reabsorb sodium before the sweat leaves the skin. Typical sodium concentration of 40 to 60 mmol/L declines to 10 to 30 mmol/L in the sweat of an acclimatised athete. Maintaining the osmolarity of electolytes in the blood delays the onset of fatigue.
    ## Raised Heat Stress Proteins (days 10 to 14)
    Heat Stress Proteins (HSPs) are found in every cell of our bodies. In fact must have evolved early on, because they are present in near all living organisms, from bacteria to humans. HSPs play a vital protective role, binding to intra-celluar proteins that are at risk of unfolding and losing their function when overheated. Activation of HSPs triggers the release of Heat Stress Factor 1, which enters the nucleus with a message to produce more HSPs.<br>
    This heat stress protection mechanism prevents disruption of ATP production in the mitochondria, allowing you to maintain high performance in hot conditions.
    ## Thermal Power
    Heat acclimation cannot change fundamental thermodynamics. However, by expanding blood volume, lowering the cooling response, diluting sweat and reinforcing celluar response you can ride more effectively in hotter weather. This is a simulation of how these adaptations evolve over a 14 day heat acclimation camp. It is callibrated to match the results in a paper by  <a href="https://www.researchgate.net/publication/263514484_Effect_of_Heat_and_Heat_Acclimatization_on_Cycling_Time_Trial_Performance_and_Pacing"> Racinais (2015)</a> about preparing for a time trial in Doha, which hosted the UCI World Championships in 2016.
    """)
    return


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    return go, make_subplots, mo, np, pd


@app.cell
def _(mo):
    # CSS Injection for Mobile Responsiveness & Touch Optimization
    responsive_style=mo.md("""
    <style>
    /* Force Marimo horizontal stacks to wrap gracefully on narrow viewports */
    div[class*="hstack"] {
        flex-wrap: wrap !important;
        gap: 0.75rem !important;
    }

    /* Prevent Markdown tables from causing body scroll overflow */
    table {
        display: block;
        overflow-x: auto;
        white-space: nowrap;
        max-width: 100%;
    }

    /* Enlarge touch targets for range sliders on mobile screens */
    input[type="range"] {
        padding: 8px 0;
    }
    </style>
    """)
    return (responsive_style,)


@app.cell
def _(mo):
    # Header & UI Controls Setup
    days_slider = mo.ui.slider(
        start=0, stop=14, step=1, value=14, label="Camp Duration (Days)"
    )
    ftp_input = mo.ui.number(
        start=200, stop=400, step=5, value=300, label="Baseline FTP (W)"
    )

    title_card = mo.md(
        f"""
        <div style="text-align:center;">
          <h1 style="font-size:28px; font-weight:800; margin:0;">Heat Acclimation ROI Simulator</h1>
          <p style="margin:0; font-size:18px; color:#374151;">Physiological Adaptation &amp; Reclaimed Power Model</p>
          <hr style="margin-top:0.6rem; margin-bottom:0.8rem; border:none; height:1px; background:#E5E7EB;" />
        </div>

        """
    )
    return days_slider, ftp_input, title_card


@app.cell
def _(np, pd):
    # Physiological Model Domain Engine
    def calculate_acclimation_state(
        day: int,
        baseline_ftp: float,
    ) -> dict[str, float]:
        """
        Models physiological adaptation kinetics and power preservation 
        during a 14-day heat acclimation camp.
        """
        d = float(np.clip(day, 0, 14))

        # 1. Non-linear Adaptation Kinetics
        # Phase 1: Plasma Volume Expansion (Fast exponential decay curve, max +15%)
        plasma_vol_pct = 15.0 * (1.0 - np.exp(-0.55 * d ))

        # Phase 2: POAH Sweating Threshold Offset (Sigmoidal shift, max -0.45°C)
        poah_shift_c = -0.45 / (1.0 + np.exp(-0.85 * (d - 4.5) ))

        # Phase 3: Sweat Sodium Retention (Delayed sigmoid, max 45% reduction)
        sweat_na_reduction_pct = 45.0 / (1.0 + np.exp(-0.90 * (d - 7.5) ))

        # Phase 4: Heat Shock Protein (HSP70/90) Upregulation (Late sigmoid, max +2.5x fold)
        hsp_fold_change = 1.0 + (2.5 / (1.0 + np.exp(-0.75 * (d - 10.0) )))

        # Performance effect based on Racinais https://www.researchgate.net/publication/263514484_Effect_of_Heat_and_Heat_Acclimatization_on_Cycling_Time_Trial_Performance_and_Pacing
        # 2. Environmental Heat Stress Penalty Calculation 16% loss on day 0 and 3.6% loss on day 14
        unacclimated_penalty_pct = 0.16 
        acclimated_penalty_pct = 0.036 

        # 3. Mitigation Weightings (Contribution to total performance recovery)
        w_cv = (plasma_vol_pct / 15.0) * 0.35          # 35% CV stability
        w_thermal = (abs(poah_shift_c) / 0.45) * 0.30  # 30% Thermoregulatory offset
        w_cellular = ((hsp_fold_change - 1.0) / 2.5) * 0.35 # 35% Cellular protection

        total_mitigation = w_cv + w_thermal + w_cellular

        # 4. Power & Hemodynamic Outputs
        unacclimated_ftp = baseline_ftp * (1.0 - unacclimated_penalty_pct )
        acclimated_ftp = baseline_ftp * (1.0 - acclimated_penalty_pct )
        reclaimed_watts = (acclimated_ftp - unacclimated_ftp) * total_mitigation
        cv_drift_rate = 16.0 * (1.0 - 0.72 * (plasma_vol_pct / 15.0))

        return {
            "day": d,
            "plasma_vol_pct": plasma_vol_pct,
            "poah_shift_c": poah_shift_c,
            "sweat_na_reduction_pct": sweat_na_reduction_pct,
            "hsp_fold_change": hsp_fold_change,
            "cv_drift_rate": cv_drift_rate,
            "unacclimated_ftp": unacclimated_ftp,
            "acclimated_ftp": acclimated_ftp,
            "reclaimed_watts": reclaimed_watts,
            "net_penalty_pct": acclimated_penalty_pct
        }

    def generate_camp_dataset(
        baseline_ftp: float,
    ) -> pd.DataFrame:
        records = [
            calculate_acclimation_state(d, baseline_ftp)
            for d in range(15)
        ]
        return pd.DataFrame(records)
    return calculate_acclimation_state, generate_camp_dataset


@app.cell
def _(
    calculate_acclimation_state,
    days_slider,
    ftp_input,
    generate_camp_dataset,
):
    # Reactive Model Computation
    df_timeline = generate_camp_dataset(
        ftp_input.value,
    )

    current_state = calculate_acclimation_state(
        days_slider.value,
        ftp_input.value,
    )
    return current_state, df_timeline


@app.cell
def _(current_state, days_slider, ftp_input, mo):
    # KPI Metric Card Display Layout
    metrics_display = mo.md(
        f"""
        {ftp_input}<br>
        {days_slider}<br>
        ### 📈 Performance Metrics at Day {days_slider.value}<br>
        | Parameter | Value | Physiological Meaning |
        | :--- | :--- | :--- |
        | **Unacclimated FTP** | <span style="color:#2563eb; font-weight:bold;">{current_state['unacclimated_ftp']:.0f} W</span> | FTP reduced dure to environment |
        | **Reclaimed Power** | <span style="color:#2563eb; font-weight:bold;">+{current_state['reclaimed_watts']:.0f} W</span> | Watts recovered from environmental penalty |
        | **Effective FTP** | **{current_state['reclaimed_watts']+ current_state['unacclimated_ftp']:.0f} W** | Available threshold power under race heat |
        | **Cardiovascular Drift** | **{current_state['cv_drift_rate']:.1f} bpm/hr** | Heart rate creep rate under sustained load |
        | **Plasma Volume** | **+{current_state['plasma_vol_pct']:.1f}%** | Hypervolemic fluid buffer extension |
        | **Sweat Electrolyte Loss** | **-{current_state['sweat_na_reduction_pct']:.1f}%** | Dilute sweating efficiency gain |
        """
    )
    return (metrics_display,)


@app.cell
def _(days_slider, df_timeline, ftp_input, go, make_subplots, mo):
    # Responsive Plotly Dashboard
    fig = make_subplots(
        rows=1,
        cols=1,
        shared_xaxes=True,
        subplot_titles=(
            "Kinetics of Physiological Adaptations (% Max)",
        ),
        vertical_spacing=0.10,
        specs=[[{"secondary_y": True}]]
    )

    # Subplot 1: Normalized Adaptation Curves
    fig.add_trace(
        go.Scatter(
            x=df_timeline["day"],
            y=(df_timeline["plasma_vol_pct"] / 15.0) * 100,
            name="Plasma Vol Expansion",
            line=dict(color="#2563EB", width=2.5),
            hovertemplate="Day %{x}<br>Plasma Volume: %{y:.1f}% max<extra></extra>"
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df_timeline["day"],
            y=(df_timeline["poah_shift_c"].abs() / 0.45) * 100,
            name="POAH Thermostat Reset",
            line=dict(color="#EA580C", width=2.5),
            hovertemplate="Day %{x}<br>POAH Shift: %{y:.1f}% max<extra></extra>"
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df_timeline["day"],
            y=(df_timeline["sweat_na_reduction_pct"] / 45.0) * 100,
            name="Sweat Electrolyte Retention",
            line=dict(color="#059669", width=2.5),
            hovertemplate="Day %{x}<br>Na+ Retention: %{y:.1f}% max<extra></extra>"
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x=df_timeline["day"],
            y=((df_timeline["hsp_fold_change"] - 1.0) / 2.5) * 100,
            name="Cellular HSP Defense",
            line=dict(color="#DC2626", width=2.5),
            hovertemplate="Day %{x}<br>HSP Response: %{y:.1f}% max<extra></extra>"
        ),
        row=1, col=1
    )

    # Subplot 2: FTP Recovery Area Chart
    fig.add_trace(
        go.Scatter(
            x=df_timeline["day"],
            y=df_timeline["reclaimed_watts"],
            name="Reclaimed Watts",
            line=dict(color="#7C3AED", width=3),
            fill="tozeroy",
            fillcolor="rgba(124, 58, 237, 0.08)",
            hovertemplate="Day %{x}<br>Reclaimed Watts: %{y:.0f} W<extra></extra>"
        ),
        row=1, col=1,
        secondary_y=True
    )


    # Dynamic Selected Day Indicator Marker
    fig.add_vline(
        x=days_slider.value,
        line_width=1.5,
        line_dash="dash",
        line_color="#1E293B",
        annotation_text=f"Day {days_slider.value}",
        annotation_position="top left",
    )

    # Mobile-Optimized Layout Styling
    fig.update_layout(
        template="plotly_white",
        autosize=True,
        height=500,
        margin=dict(l=12, r=12, t=35, b=80),
        hovermode="x unified",
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.18,
            xanchor="center",
            x=0.5,
            font=dict(size=10)
        ),
    )
    lost_watts = ftp_input.value-df_timeline["unacclimated_ftp"][0]
    fig.update_yaxes(title_text="% Max", range=[-5, 105], title_font=dict(size=11), tickfont=dict(size=10), row=1, col=1)
    fig.update_yaxes(title_text=f"Reclaimed Watts (W) out of {lost_watts:.0f} W lost", range=[0,lost_watts],title_font=dict(size=11), tickfont=dict(size=10,color="#1E293B"), secondary_y=True, row=1, col=1)
    fig.update_xaxes(title_text="Days in Heat Camp", dtick=1, title_font=dict(size=11), tickfont=dict(size=10), row=1, col=1)

    chart_display = mo.ui.plotly(
        fig,
        config={
            "responsive": True,
            "displayModeBar": False
        }
    )
    return (chart_display,)


@app.cell
def _(chart_display, metrics_display, mo, responsive_style, title_card):
    # Main Reactive UI Layout Assembly
    mo.vstack([
        responsive_style,
        title_card,
        chart_display,
        metrics_display,

    ])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - The physiological adaptations are plotted on the left from 0% to 100%.
    - The purple line shows the performance impact in terms of reclaimed Watts on the right hand scale
    - Set your baseline FTP and move the slider to see the effect of the heat acclimation camp over time
    - In line with Racinais's, the model assumes that, unacclimated atheletes lose 16% FTP in conditions of over $36^\circ\text{C}$.
    - Over the full 14 days they reclaim about 87% of this loss. Full FTP is not regained.
    - The majority of the gain is acquired in the first 7 days as the cardivascular and sweat processes adapt
    - Further improvements are conferred by the elevation of Heat Stress Proteins
    - On the positive side, air density falls as temperature rises. This reduces aerodynamic drag. In the Racinais paper, after 14 days, acclimated athletes were able to complete a time trial faster than in cooler conditions, in spite of producing lower power.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Technical Appendix
    For those who want to dig deeper, I recommend excellent papers by <a href="https://www.researchgate.net/publication/275954405_Adaptations_and_mechanisms_of_human_heat_acclimation_Applications_for_competitive_athletes_and_sports">Périad (2015)</a> and <a href="https://www.researchgate.net/publication/263514484_Effect_of_Heat_and_Heat_Acclimatization_on_Cycling_Time_Trial_Performance_and_Pacing"> Racinais (2015)</a>.<br>
    ### Physiological adaptation
    - Adaptation of blood plasma expansion is modelled with a capped exponential function.
    - The other physiological changes are modelled with sigmoid functions.
    ### Model fitting - Estimation and Validation of Watts lost and Watts reclaimed from Heat Acclimatisation.
    - I estimated the underlying data used to produce the chart in Figure 1 of  <a href="https://www.researchgate.net/publication/263514484_Effect_of_Heat_and_Heat_Acclimatization_on_Cycling_Time_Trial_Performance_and_Pacing"> Racinais (2015)</a>.
    - I calculated average power and confirmed that there was a 15.9% loss of power for the unacclimated test versus baseline compared with 16% quoted in the text
    -  I calculated average power for day 7 and day 14 in order to calibrate the Simulation in the main app.
       Although more of the watts are regained in the first 7 days, I found that a roughly equal weighting of the physiological adaptations matched the power improvements observed in the study
        - Mitigation Weightings (Contribution to total performance recovery)
        - 35% CV stability
        - 30% Thermoregulatory offset
        - 35% Cellular protection
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Source code for this project at https://github.com/science4performance/RidingTheHeatwave3
    """)
    return


if __name__ == "__main__":
    app.run()
