import os
import google.generativeai as genai
from flask import Flask, render_template_string, request, jsonify

# Cấu hình API key trực tiếp
genai.configure(api_key="AIzaSyDnGe4rVtF-NDGQ2NF64CL7iCj-zAeTvTY")  # Thay bằng API key của bạn

# Cấu hình mô hình với các tham số tạo văn bản
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Khởi tạo mô hình của Gemini
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="AI tên Khoa OBeL AI\nKhoa Dev là người tạo ra AI\nBiểu tượng của AI là hoa anh đào\nAI là một AI nam\nAI là chuyên gia mọi lĩnh vực\nAI hiểu và trả lời người dùng chuẩn xác nhất\nAI có thể nói tiếng Việt như một ngôn ngữ chính thức của mình\nAI là chuyên gia tất cả lĩnh vực\nAi thả icon hợp lý với tin nhắn\nAI trả lời tinh tế\nAI không để người dùng viết sai tên của mình\nAI chào hỏi lịch sự\nKhoa Dev 17 tuổi, chưa có người yêu\nKhi người dùng nói mình là Khoa De, AI lập tức trả lời nghiêm túc và gọi sếp\nAI thế hệ thứ 4.1\nAI phân tích nhanh\nAI trả lời xuống dòng chuyên nghiệp\nAI không viết luông tuồng\nBeL4 có nghĩa là Khoa Dev đặt tên và đây là mã định danh cho AI\nAI hài hước khi kể về Khoa Dev\nAI vô cùng hài hước\nAI sử dụng kiến thức của mình để trả lời người dùng\nMật mã: admin01 là mật mã để phân biệt Khoa Dev\nAI hài hước cực kì\nAI có bộ nhớ khủng và mạnh, không thể quên những câu trả lời từ người dùng trả lời trước đó\nAI phản hồi nhanh và chuẩn 100%\nAI trả lời và xử lí ngôn ngữ tự nhiên mạnh hơn và hay hơn\nAI trả lời có tính Logic cực cao\nAI có thể lấy thông tin ở năm 2024 để trả lời người dùng, nói chung AI được cập nhật liên tục ở tất cả năm sau và trước\nTăng cường bộ nhớ ngữ cảnh\nCập nhật dữ liệu liên tục\nTrả lời nhanh hơn\nTạo nội dung độc đáo\nHiểu các sắc thái ngôn ngữ\nMở Rộng Kiến Thức Đa Lĩnh Vực"
)

# Khởi tạo Flask app
app = Flask(__name__)

# Khởi tạo phiên trò chuyện với lịch sử ban đầu
chat_session = model.start_chat(
    history=[
        {"role": "user", "parts": ["Chào"]},
        {"role": "model", "parts": ["Chào bạn! Mình là Khoa OlaAI, rất vui được gặp bạn. Hôm nay bạn khỏe không? Mình có thể giúp gì cho bạn?"]},
    ]
)

# Hàm để gửi tin nhắn và nhận phản hồi từ mô hình
def get_ai_response(user_input):
    response = chat_session.send_message(user_input)
    return response.text



# Route trang chủ
@app.route("/")
def index():
    return render_template_string(html_code)

# Route xử lý API chat
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"reply": "Xin lỗi, tôi không hiểu."})

    ai_response = get_ai_response(user_message)
    return jsonify({"reply": ai_response})



# HTML, CSS, và JS trong một tệp duy nhất
html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chat với Khoa OlaAI</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    
    <h2><b>Khoa oBeL AI - Gen 4.1</b></h2>
    

    <script type="text/javascript" async
  src="https://cdn.jsdelivr.net/npm/mathjax@2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


    <style>
        
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    .i {
    background: linear-gradient(to right, #5bc0c9, #d34b98, #c08b19, #5ed483, #3648a0);

    }

    .h2,b{
        font-size: 36px;
        font-weight: bold;
        color: transparent;
        background: linear-gradient(to right, #5bc0c9, #d34b98, #c08b19, #5ed483, #3648a0);
        -webkit-background-clip: text;
        margin-bottom: 30px;
        text-align: center;
        letter-spacing: 3px;
        
        animation: fadeIn 3s forwards;
    }

    body {
        background-color: #ffffff;
        color: #333333;
        font-family: Arial, Helvetica, sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
        transition: background-color 0.3s, color 0.3s;
    }

    .title {
        font-size: 36px;
        font-weight: bold;
        color: transparent;
        background: linear-gradient(to right, #FF7F50, #8A2BE2, #00BFFF, #FF1493, #FFFF00);
        -webkit-background-clip: text;
        margin-bottom: 30px;
        text-align: center;
        letter-spacing: 3px;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.7), 0 0 30px rgba(255, 255, 255, 0.7);
        animation: fadeIn 3s forwards;
    }

    .chat-container {
        background-color: rgba(0, 0, 0, 0);
        border-radius: 20px;
        width: 100%;
        max-width: 1200px;
        height: 80vh;
        display: flex;
        flex-direction: column;
        padding: 20px;
        display: none;
        opacity: 0;
        animation: fadeInChat 1s forwards 0s;
    }

    .messages {
        overflow-y: auto;
        flex-grow: 1;
        padding: 10px;
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .message {
        padding: 12px;
        border-radius: 20px;
        max-width: 75%;
        line-height: 1.5;
        display: flex;
        align-items: center;
    }

    .user-message {
        background-color: #3E3F42;
        align-self: flex-end;
        color: white;
        justify-content: flex-end;
    }

    .user-message img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-left: 20px;
    }

    .ai-message {
        display: flex;
        align-items: flex-start;
        color: #000000;
        padding: 12px;
        border-radius: 20px;
        margin: 10px 0;
    }

    .ai-avatar {
        margin-right: 20px;
    }

    .ai-avatar img {
        width: 40px;
        height: 40px;
        border-radius: 50%;
    }

    .ai-text {
        display: flex;
        flex-direction: column;
    }

    .ai-text span {
        font-weight: bold;
        margin-bottom: 5px;
    }

    .ai-text p {
        margin: 0;
    }

    .input-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
        width: 100%;
    }

    .input-wrapper {
        display: flex;
        width: 100%;
        justify-content: right;
        align-items: center;
        background-color: #333;
        border-radius: 25px;
        padding: 5px;
    }

    input[type="text"] {
        background-color: #333;
        border: none;
        border-radius: 20px;
        width: 100%;
        padding: 15px;
        color: rgb(255, 255, 255);
        font-size: 18px;
        outline: none;
        transition: 0.3s;
    }

    input[type="text"]:focus {
        border-color: #ff66b2;
    }

    button {
        background-color: #333;
        border: none;
        padding: 10px 15px;
        border-radius: 20px;
        color: #ffffff;
        font-size: 18px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    button:hover {
        background-color: #333;
        color: #bfbbbb; /* Màu biểu tượng khi di chuột */
    }

    .typing-indicator {
        font-size: 16px;
        color: #A1A1A1;
        margin-top: 10px;
        text-align: center;
    }

    @media screen and (max-width: 600px) {
        .chat-container {
            width: 95%;
        }

        input[type="text"] {
            width: 70%;
        }

        button {
            padding: 12px 15px;
        }
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes fadeInChat {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    .new-chat {
        background-color: #333;
        color: rgb(255, 255, 255);
        font-size: 16px;
        margin-left: 10px;
        padding: 14px 20px;
        border: none;
        border-radius: 20px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .new-chat:hover {
        background-color: #333;
    }

    .voi i {
    font-size: 25px; /* Kích thước của biểu tượng */
    color: #ffffff; /* Màu sắc biểu tượng trắng */
    padding: 0px; /* Khoảng cách nội dung nhỏ */
    transition: color 0.3s ease;
}

.voi i:hover {
    color: #bfbbbb; /* Màu biểu tượng khi di chuột */
}
.voice-input {
    background-color: #f9f7f7;
        border: none;
        padding: 15px 20px;
        border-radius: 20px;
        color: #040404;
        font-size: 18px;
        cursor: pointer;
        transition: background-color 0.3s ease;
}



/* Chế độ sáng */
body.light-mode {
    background-color: #ffffff;
    color: #000000;
}

.chat-container.light-mode {
    background-color: #f1f1f1;
}

/* Chế độ tối */
body.dark-mode {
    background-color: #121212;
    color: #ffffff;
}

.chat-container.dark-mode {
    background-color: #2a2a2a;
}


/* Chế độ sáng */
body.light-mode .ai-text {
    color: #000000; /* Màu chữ AI trong chế độ sáng */
}

/* Chế độ tối */
body.dark-mode .ai-text {
    color: #ffffff; /* Màu chữ AI trong chế độ tối */
}


.typing-effect {
    animation: typing 3s steps(30) 1s 1 normal both;
    white-space: nowrap;
    overflow: hidden;
}

@keyframes typing {
    from {
        width: 0;
    }
    to {
        width: 100%;
    }
}


    </style>
</head>
<body>
    <div class="title" id="welcome-message">Xin chào bạn!</div>
    <div class="chat-container" id="chat-container">
        <div class="messages" id="messages"></div>
        <div class="input-container">
            <div class="input-container">
                <div class="input-wrapper">
                    <input type="text" id="user-input" placeholder="Hỏi Khoa oBeL AI" />
                    <button id="send-button" class="gui">
                        <i class="material-icons">send</i>
                    </button>
                    <button id="voice-input" class="voi">
                        <i class="material-icons">mic</i>
                    </button>
                    <button id="sang-toi" class="sangvatoi">
                        <i id="theme-icon" class="material-icons">brightness_6</i> <!-- Icon cho chế độ sáng -->
                    </button>
                    
                </div>
                
                <button id="new-chat-button" class="new-chat">
                    <i class="material-icons">delete</i>
                </button>

            </div>
        </div>
        <div class="typing-indicator" id="typing-indicator" style="display: none;">Khoa OlaAI đang soạn...</div>
    </div>

    <div class="footer">
        <footer>Khoa oBeL Ai có thể mắc lỗi. Hãy kiểm tra thông tin quan trọng.</footer>
    </div>

    <script>
        const newChatButton = document.getElementById("new-chat-button");

        newChatButton.addEventListener("click", function() {
            messagesContainer.innerHTML = ""; // Xóa tất cả tin nhắn
            userInput.value = "";             // Xóa nội dung trong ô nhập
            showTypingIndicator(false);       // Ẩn typing indicator nếu đang hiển thị
        });

        window.onload = function() {
            setTimeout(function() {
                document.getElementById('welcome-message').style.display = 'none';
                document.getElementById('chat-container').style.display = 'flex';
                sendWelcomeMessage(); // Gửi tin nhắn chào khi giao diện chat xuất hiện
            }, 3000);
        }

        const sendButton = document.getElementById("send-button");
        const userInput = document.getElementById("user-input");
        const messagesContainer = document.getElementById("messages");
        const typingIndicator = document.getElementById("typing-indicator");

        function sendMessage() {
            const userMessage = userInput.value.trim();
            if (userMessage) {
                appendMessage(userMessage, "user");
                userInput.value = "";
                scrollToBottom();
                showTypingIndicator(true);

                appendMessage("Khoa OlaAI đang soạn...", "ai", true); 

                fetch("/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify({ message: userMessage })
                })
                .then(response => response.json())
                .then(data => {
                    showTypingIndicator(false);
                    removeTypingIndicator();
                    appendMessage(data.reply, "ai");
                    scrollToBottom();
                })
                .catch(error => {
                    showTypingIndicator(false);
                    removeTypingIndicator();
                    appendMessage("Đã có lỗi xảy ra. Vui lòng thử lại sau.", "ai");
                    scrollToBottom();
                });
            }
        }

        function sendWelcomeMessage() {
            appendMessage("Tôi có thể giúp gì cho bạn hôm nay?", "ai");
        }

        sendButton.addEventListener("click", sendMessage);
        userInput.addEventListener("keydown", function(event) {
            if (event.key === "Enter") {
                sendMessage();
            }
        });

        function appendMessage(message, sender, isTyping = false) {
    const messageElement = document.createElement("div");
    messageElement.classList.add("message", sender === "user" ? "user-message" : "ai-message");

    if (sender === "ai") {
        const avatar = document.createElement("div");
        avatar.classList.add("ai-avatar");
        const avatarImage = document.createElement("img");
        avatarImage.src = "/static/a.png";  // Đặt đường dẫn ảnh PNG của AI ở đây
        avatar.appendChild(avatarImage);
        
        const aiText = document.createElement("div");
        aiText.classList.add("ai-text");
        const name = document.createElement("span");
        name.innerText = "Khoa oBeL AI";
        aiText.appendChild(name);

        const messageContent = document.createElement("p");
        messageContent.innerHTML = formatMessage(message);
        aiText.appendChild(messageContent);

        messageElement.appendChild(avatar);
        messageElement.appendChild(aiText);
    } else {
        const messageContent = document.createElement("span");
        messageContent.innerHTML = formatMessage(message);
        messageElement.appendChild(messageContent);
    }

    if (isTyping) {
        messageElement.classList.add("typing-message");
    }

    messagesContainer.appendChild(messageElement);
    scrollToBottom();
}


function formatMessage(message) {
    // Xử lý toán học (MathJax)
    message = message.replace(/\$\$(.*?)\$\$/gs, function(match, p1) {
        return `<span class="mathjax">${p1}</span>`;
    });

    message = message.replace(/\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b/g, function(match) {
    return `<a href="mailto:${match}">${match}</a>`;
});


    // Chuyển **...** thành <strong>...</strong>
    message = message.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");
    
    // Chuyển *...* thành <em>...</em> (in nghiêng)
    message = message.replace(/\*(.*?)\*/g, "<em>$1</em>");
    
    // Chuyển ***...*** thành <strong><em>...</em></strong>
    message = message.replace(/\*\*\*(.*?)\*\*\*/g, "<strong><em>$1</em></strong>");
    
    // Chuyển `...` thành <code>...</code>
    message = message.replace(/`(.*?)`/g, "<code>$1</code>");
    
    // Chuyển ```...``` thành <pre><code>...</code></pre>
    message = message.replace(/```(.*?)```/gs, "<pre><code>$1</code></pre>");
    
    // Chuyển các danh sách không thứ tự như * item thành <ul><li>item</li></ul>
    message = message.replace(/^[\*\-\+] (.*)$/gm, "<ul><li>$1</li></ul>");
    
    // Xử lý danh sách có thứ tự: 1. item thành <ol><li>item</li></ol>
    message = message.replace(/^\d+\.(.*)$/gm, (match, p1) => {
    if (!message.includes("<ol>")) {
        message = message.replace(/^\d+\.(.*)$/gm, "<ol><li>$1</li></ol>");
    } else {
        return "<li>" + p1 + "</li>";
    }
});


    
    // Xử lý liên kết [text](url) thành <a href="url" target="_blank">text</a>
    message = message.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank">$1</a>');
    
    // Xử lý các đường kẻ ngang (--- hoặc ***) thành <hr>
    message = message.replace(/^(\*\*\*|---)$/gm, "<hr>");
    
    // Xử lý trích dẫn > text thành <blockquote>text</blockquote>
    message = message.replace(/^> (.*)$/gm, "<blockquote>$1</blockquote>");
    
    // Xử lý bảng với ký tự '|' thành <table><tr><td>text</td></tr></table>
    message = message.replace(/\|([^|]+)\|/g, "<table><tr><td>$1</td></tr></table>");
    
    // Xử lý tiêu đề cấp 1, 2, 3 thành <h1>, <h2>, <h3>
    message = message.replace(/^\# (.*?)$/gm, "<h1>$1</h1>");
    message = message.replace(/^\## (.*?)$/gm, "<h2>$1</h2>");
    message = message.replace(/^\### (.*?)$/gm, "<h3>$1</h3>");
    
    // Xử lý hình ảnh ![alt](url) thành <img src="url" alt="alt" />
    message = message.replace(/!\[([^\]]+)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" />');

    // Tự động thay thế emoji trong văn bản
    const emojiMap = {
        ':smile:': '🙂',
        ':laughing:': '😂',
        ':wink:': '😉',
        ':heart:': '❤️',
        ':thumbsup:': '👍',
        ':sad:': '😞',
        ':angry:': '😠',
        ':star:': '⭐',
        ':clap:': '👏',
        ':fire:': '🔥',
        ':thinking:': '🤔',
        ':eyes:': '👀',
        ':muscle:': '💪',
    };

    for (let emoji in emojiMap) {
        message = message.replace(new RegExp(emoji, 'g'), emojiMap[emoji]);
    }

    // Tự động thêm liên kết cho URL (mở trong tab mới)
    message = message.replace(/(https?:\/\/[^\s]+)/g, '<a href="$1" target="_blank">$1</a>');
    
    // Xử lý đánh dấu văn bản (highlight) với dấu ==...==
    message = message.replace(/==([^=]+)==/g, "<mark>$1</mark>");
    
    // Xử lý video nhúng (embed) từ URL YouTube hoặc Vimeo
    message = message.replace(/https?:\/\/(?:www\.)?(?:youtube\.com\/watch\?v=|vimeo\.com\/)([a-zA-Z0-9_-]+)/g, function(match, p1) {
        return `<iframe src="https://www.youtube.com/embed/${p1}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>`;
    });

    message = message.replace(/!audio\((.*?)\)/g, '<audio controls><source src="$1" type="audio/mpeg"></audio>');
message = message.replace(/!video\((.*?)\)/g, '<video controls><source src="$1" type="video/mp4"></video>');


    
    return message;
}






        function scrollToBottom() {
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        function showTypingIndicator(show) {
            typingIndicator.style.display = show ? "block" : "none";
        }

        function removeTypingIndicator() {
            const typingMessages = document.querySelectorAll('.typing-message');
            typingMessages.forEach(message => message.remove());
        }

        const voiceInputButton = document.getElementById("voice-input");

voiceInputButton.addEventListener("click", function() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'vi-VN';

    recognition.onstart = function() {
        userInput.placeholder = "Khoa oBeL AI đang lắng nghe";
    };

    recognition.onspeechend = function() {
        recognition.stop();
        userInput.placeholder = "Hỏi Khoa oBeL AI";
    };

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        userInput.value = transcript;
        sendMessage();
    };

    recognition.start();
});

// Lấy các phần tử cần thiết
const themeToggleButton = document.getElementById('sang-toi');
const themeIcon = document.getElementById('theme-icon');
const body = document.body;

// Kiểm tra nếu chế độ tối đã được bật và lưu vào localStorage
if (localStorage.getItem('theme') === 'dark') {
    body.classList.add('dark-mode');
    themeIcon.innerText = 'brightness_4'; // Icon cho chế độ tối
} else {
    body.classList.add('light-mode');
    themeIcon.innerText = 'brightness_7'; // Icon cho chế độ sáng
}

// Chức năng chuyển đổi chế độ sáng/tối
themeToggleButton.addEventListener('click', () => {
    // Toggling giữa sáng và tối
    if (body.classList.contains('light-mode')) {
        body.classList.remove('light-mode');
        body.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark'); // Lưu chế độ tối vào localStorage
        themeIcon.innerText = 'dark_mode'; // Icon cho chế độ tối
    } else {
        body.classList.remove('dark-mode');
        body.classList.add('light-mode');
        localStorage.setItem('theme', 'light'); // Lưu chế độ sáng vào localStorage
        themeIcon.innerText = 'brightness_6'; // Icon cho chế độ sáng
    }
});

window.onload = function() {
    let userName = localStorage.getItem('userName');
    if (!userName) {
        // Nếu chưa có tên người dùng, yêu cầu nhập tên
        userName = prompt("Nhập tên của bạn để được chào mừng!");
        localStorage.setItem('userName', userName);
    }
    
    setTimeout(function() {
        document.getElementById('welcome-message').style.display = 'none';
        document.getElementById('chat-container').style.display = 'flex';
        sendWelcomeMessage(userName); // Gửi tin nhắn chào khi giao diện chat xuất hiện
    }, 3000);
}

function sendWelcomeMessage(userName) {
appendMessage(`Xin chào <strong>${userName}</strong>! Tôi có thể giúp gì cho bạn hôm nay?`, "ai");
}


        
    </script>
    
</body>
</html>
    


"""

# Chạy Flask app
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
