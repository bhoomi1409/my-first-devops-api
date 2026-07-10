import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="FireAgent Call Dashboard", layout="wide", page_icon="🔥")
st.title("🔥 FireAgent Voice Operations Dashboard")
st.markdown("Monitor latency, transcripts, sentiment, and cost-per-call in real-time. (Phase 8 Observability MVP)")

# In a real app, this would be fetched from a PostgreSQL or MongoDB database
# where your orchestration layer logs every call event.
mock_calls = [
    {
        "call_id": "CALL_101",
        "persona": "FireReach SDR",
        "duration_sec": 145,
        "sentiment": "Positive",
        "stt_latency_ms": 320,
        "llm_latency_ms": 450,
        "tts_latency_ms": 180,
        "cost_stt": 0.010,
        "cost_llm": 0.002,
        "cost_tts": 0.150,
        "transcript": [
            {"role": "assistant", "text": "Hi, this is Alex from FireReach. How are you today?"},
            {"role": "user", "text": "I'm good, just a bit busy. What's this about?"},
            {"role": "assistant", "text": "I'll be quick! We help sales teams automate their outbound calling using voice AI. Are you currently exploring AI for your SDRs?"},
            {"role": "user", "text": "Actually yes, we are looking into Bolna and Vapi right now."},
            {"role": "assistant", "text": "Perfect timing then. FireReach gives you that exact architecture but fully managed, with roleplay scoring built-in. Would you be open to a 10-minute demo next week?"},
            {"role": "user", "text": "Sure, send me an invite for Tuesday."}
        ]
    },
    {
        "call_id": "CALL_102",
        "persona": "Friendly Support",
        "duration_sec": 45,
        "sentiment": "Resolved",
        "stt_latency_ms": 300,
        "llm_latency_ms": 600,
        "tts_latency_ms": 200,
        "cost_stt": 0.003,
        "cost_llm": 0.001,
        "cost_tts": 0.040,
        "transcript": [
            {"role": "assistant", "text": "Support, how can I help?"},
            {"role": "user", "text": "I can't log in!"},
            {"role": "assistant", "text": "I'm sorry to hear that. I've just sent a password reset link to your email. Can you check if it arrived?"},
            {"role": "user", "text": "Got it, thanks. That was fast."}
        ]
    }
]

# Sidebar metrics
st.sidebar.header("Aggregated Metrics")
total_calls = len(mock_calls)
avg_duration = sum([c["duration_sec"] for c in mock_calls]) / total_calls
total_cost = sum([c["cost_stt"] + c["cost_llm"] + c["cost_tts"] for c in mock_calls])

st.sidebar.metric("Total Calls Today", total_calls)
st.sidebar.metric("Avg Duration (s)", f"{avg_duration:.0f}s")
st.sidebar.metric("Total Spend", f"${total_cost:.3f}")

st.sidebar.markdown("---")
st.sidebar.markdown("**Latency Averages:**")
avg_stt = sum([c["stt_latency_ms"] for c in mock_calls]) / total_calls
avg_llm = sum([c["llm_latency_ms"] for c in mock_calls]) / total_calls
avg_tts = sum([c["tts_latency_ms"] for c in mock_calls]) / total_calls
st.sidebar.metric("STT (Endpointing)", f"{avg_stt:.0f}ms")
st.sidebar.metric("LLM (Time-to-first-token)", f"{avg_llm:.0f}ms")
st.sidebar.metric("TTS (Time-to-first-chunk)", f"{avg_tts:.0f}ms")
st.sidebar.metric("Total Turnaround Time", f"{(avg_stt + avg_llm + avg_tts):.0f}ms")

# Main content
st.subheader("Call Logs")

for call in mock_calls:
    # Emoji based on sentiment
    sentiment_icon = "🟢" if call["sentiment"] in ["Positive", "Resolved"] else "🔴"
    
    with st.expander(f"📞 {call['call_id']} | {call['persona']} | {call['duration_sec']}s | {sentiment_icon} {call['sentiment']}"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Latency Breakdown:**")
            st.write(f"- STT Endpointing: `{call['stt_latency_ms']} ms`")
            st.write(f"- LLM TTFT: `{call['llm_latency_ms']} ms`")
            st.write(f"- TTS TTFC: `{call['tts_latency_ms']} ms`")
            st.write(f"- **Total Perceived Latency:** `{call['stt_latency_ms'] + call['llm_latency_ms'] + call['tts_latency_ms']} ms`")
            
        with col2:
            st.markdown("**Cost Breakdown:**")
            st.write(f"- STT: `${call['cost_stt']:.3f}`")
            st.write(f"- LLM: `${call['cost_llm']:.3f}`")
            st.write(f"- TTS: `${call['cost_tts']:.3f}`")
            st.write(f"- **Total Call Cost:** `${call['cost_stt'] + call['cost_llm'] + call['cost_tts']:.3f}`")
            
        st.markdown("---")
        st.markdown("**Transcript:**")
        for msg in call["transcript"]:
            if msg["role"] == "assistant":
                st.info(f"**🤖 AI:** {msg['text']}")
            else:
                st.success(f"**👤 User:** {msg['text']}")
