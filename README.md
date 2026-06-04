\# 🤖 AI \& Tech SMM Post Generatoru



> Automated SMM Post Generator — n8n, Groq LLM (LLaMA 3.3) və Streamlit istifadə edərək AI əsaslı sosial media məzmun generatoru qurdum. RSS feed-dən avtomatik xəbər çəkir, Azərbaycan dilində Instagram postları yazır, Telegram bot vasitəsilə təsdiqləmə sistemi işləyir.



🔗 \*\*Canlı demo:\*\* https://ai-smm-post-generator-bdbkwc46nh48r2ycatqt3j.streamlit.app



\---



\## ✅ Tamamlanma Kriteriyaları



\- \[x] RSS feed-dən məqalə avtomatik çəkilir

\- \[x] Groq LLM ilə Azərbaycan dilində post generasiya edilir

\- \[x] Telegram-a avtomatik bildiris göndərilir

\- \[x] Telegram-da ✅ Yayımla / ❌ Rədd et düymələri işləyir

\- \[x] Streamlit dashboard-da 3 post variantı generasiya edilir

\- \[x] Streamlit Cloud-da deploy edilib, public link mövcuddur



\---



\## 🛠 Texnologiya Xəritəsi



| Texnologiya | Rolu |

|---|---|

| \*\*n8n\*\* | Workflow avtomatlaşdırma — RSS, API, Telegram inteqrasiyası |

| \*\*Groq API (LLaMA 3.3)\*\* | Azərbaycan dilində AI post generasiyası |

| \*\*Telegram Bot API\*\* | Bildiriş və təsdiqləmə sistemi |

| \*\*Streamlit\*\* | Veb interfeys — AI ilə vibe coding üsulu ilə yazılıb |

| \*\*Docker\*\* | n8n mühitinin qurulması |

| \*\*Python\*\* | Streamlit tətbiqinin əsası |



\---



\## ⚠️ Risklər və Həllər



| Risk | Həll |

|---|---|

| API quota limiti | Groq-un yüksək limitli pulsuz planı istifadə edildi |

| Encoding xətası | Latın əlifbası filter və sistem prompt ilə həll edildi |

| Webhook xarici əlçatanlıq | ngrok ilə localhost internet üzərindən açıldı |



\---



\## 🚀 İnkişaf İstiqamətləri



\- \*\*v1\*\* — RSS + AI + Telegram ✅ (tamamlandı)

\- \*\*v2\*\* — Streamlit dashboard + post generatoru ✅ (tamamlandı)

\- \*\*v3\*\* — Buffer/Meta API ilə Instagram-a avtomatik post atmaq



\---



\## 👷 Əvəz Olunan İxtisas



Bu layihə SMM mütəxəssisinin gündəlik məzmun hazırlama işini qismən avtomatlaşdırır — post yazmaq, redaktə etmək və planlaşdırmaq üçün sərf olunan vaxtı əhəmiyyətli dərəcədə azaldır.

