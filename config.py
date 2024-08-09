# utils/config.py

# Ngưỡng cho các lớp liên quan đến nội dung NSFW
NSFW_THRESHOLDS = {
    'hentai': 0.5,
    'porn': 0.5,
    'sexy': 0.5
}

# Các lớp của mô hình
NSFW_LABELS = ['drawings', 'hentai', 'neutral', 'porn', 'sexy']
