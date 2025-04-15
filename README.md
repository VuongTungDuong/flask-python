# Using pydantic V2
Flask Không hộ trỡ viết API docs với Pydantic. Dùng apiDog để test vào tạo api.json

# Build Dự án bằng docker
docker compose up -d

#  Run Server Developer need attach container
## Cài PKG
```
pdm install
```

## Chạy server
```
pdm start
```

# Attach SQL
```
docker exce -it <name_container> bash
```

# Access DB

```
psql -U postgres -d flask
```

## Migrates
Cần chạy khi có migrest mới mỗi tệp theo thời gian
