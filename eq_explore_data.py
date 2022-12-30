import json

# 探索数据的结构
filename = 'data/earthquake/eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

# 用所给 json 数据创建易于阅读的数据
# readable_file = 'data/earthquake/readable_eq_data_30_day_m1.json'
# with open(readable_file, 'w') as f:
#     json.dump(all_eq_data, f, indent=4)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

# for eq_dict in all_eq_dicts:
#     print(eq_dict)
#     print('\n')

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)


if __name__ == '__main__':
    print(mags[:10])
    print(titles[:2])
    print(lons[:5])
    print(lats[:5])