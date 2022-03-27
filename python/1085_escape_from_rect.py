#BOJ 1085 B3 escape_from_rect

x, y, w, h = map(int, input().split())

x_distance = min(x, w - x)
y_distance = min(y, h - y)

print(min(x_distance, y_distance))

#compressed ver.

x, y, w, h = map(int, input().split())

print(min(min(x, w - x), min(y, h - y)))
