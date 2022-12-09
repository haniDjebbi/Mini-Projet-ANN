mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
primaryColor = '#7792E3'\n\
backgroundColor = '#273346'\n\
secondaryBackgroundColor = '#B9F1C0'\n\
textColor = '#FFFFFF'\n\
font = "sans serif"\n\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml