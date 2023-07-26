class FieldConf(object):
    # 字段
    uuid = 'uuid'  # 唯一业务id，对url做md5取值
    article_url = 'article_url'  # 链接
    project_title = '标题'  # 标题
    publish_time = '时间'  # 发布时间
    area = '地区'  # 地区
    content = '正文'  # 正文
    announcement = '招标公告名'  # 招标公告名
    bid_finish_time = '招标时间'  # 招标时间
    bid_condition = '招标条件'  # 招标条件
    project_name = '项目名称'  # 项目名称
    construction_location = '建设地点'  # 建设地点
    scale = '建设项目规模'  # 建设项目规模
    tender_price = '项目招标控制价'  # 项目招标控制价
    duration = '计划工期'  # 计划工期
    bid_section = '标段划分'  # 标段划分
    bid_scope = '招标范围'  # 招标范围
    bid_evaluation_rule = '投标人资格要求'  # 投标人资格要求
    receive = '招标文件的领取'  # 招标文件的领取
    submit = '投标文件的递交'  # 投标文件的递交
    medium = '发布公告的媒介'  # 发布公告的媒介
    other_requirements = '其他要求或说明'  # 其他要求或说明
    tender_unit = '招标人'  # 招标人
    tender_unit_tel = '招标人联系方式'  # 招标人联系方式
    agency = '招标代理'  # 招标代理
    bid_agency_tel = '招标代理联系方式'  # 招标代理联系方式
    bid_status = '招标状态'  # 招标状态
    bid_result = '中标结果'  # 中标结果
    bid_winner = '中标单位'  # 中标单位
    win_bid_price = '中标价'  # 中标价
    primary_indicators = '一级指标'
    secondary_indicators = '二级指标'
    source_code = '源码'

    field_dict = {
        'uuid': 'uuid',  # 唯一业务id，对url做md5取值
        'article_url': 'article_url',  # 链接
        'title': '标题',  # 标题
        'project_number': '项目编号',  # 项目编号
        'publish_time': '时间',  # 发布时间
        'area': '地区',  # 地区
        'content': '正文',  # 正文
        'announcement': '招标公告名',  # 招标公告名
        'bid_finish_time': '招标时间',  # 招标时间
        'bid_condition': '招标条件',  # 招标条件
        'project_name': '项目名称',  # 项目名称
        'construction_location': '建设地点',  # 建设地点
        'scale': '建设项目规模',  # 建设项目规模
        'tender_price': '项目招标控制价',  # 项目招标控制价
        'duration': '计划工期',  # 计划工期
        'bid_section': '标段划分',  # 标段划分
        'bid_scope': '招标范围',  # 招标范围
        'bid_evaluation_rule': '投标人资格要求',  # 投标人资格要求
        'receive': '招标文件的领取',  # 招标文件的领取
        'submit': '投标文件的递交',  # 投标文件的递交
        'medium': '发布公告的媒介',  # 发布公告的媒介
        'other_requirements': '其他要求或说明',  # 其他要求或说明
        'tender_unit': '招标人',  # 招标人
        'tender_unit_tel': '招标人联系方式',  # 招标人联系方式
        'agency': '招标代理',  # 招标代理
        'bid_agency_tel': '招标代理联系方式',  # 招标代理联系方式
        'bid_status': '招标状态',  # 招标状态
        'bid_result': '中标结果',  # 中标结果
        'bid_winner': '中标单位',  # 中标单位
        'win_bid_price': '中标价',  # 中标价
        # 'primary_indicators': '一级指标',
        # 'secondary_indicators': '二级指标',
        'source_code': '源码',
        'channel': '所属频道',
        't1_name': '一级分类',
        't2_name': '二级分类',
        't3_name': '三级分类',
        'industry': '所属行业',
    }
    key_list = [
                {
                    "name": "工程类",
                    "is_show": 1,
                    "sid": "4000001",
                    "pid": "0",
                    "list": [
                        {
                            "name": "建筑工程",
                            "is_show": 1,
                            "sid": "4000005",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "土石方",
                                    "is_show": 1,
                                    "sid": "4000006",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "地基处理",
                                    "is_show": 1,
                                    "sid": "4000007",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "爆破",
                                    "is_show": 1,
                                    "sid": "4000008",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "拆除",
                                    "is_show": 1,
                                    "sid": "4000009",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "土建",
                                    "is_show": 1,
                                    "sid": "4000010",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "电气",
                                    "is_show": 1,
                                    "sid": "4000011",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "给水",
                                    "is_show": 1,
                                    "sid": "4000012",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "排水",
                                    "is_show": 1,
                                    "sid": "4000013",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "钢结构",
                                    "is_show": 1,
                                    "sid": "4000014",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "通风",
                                    "is_show": 1,
                                    "sid": "4000015",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "空调",
                                    "is_show": 1,
                                    "sid": "4000016",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "室内装饰装修",
                                    "is_show": 1,
                                    "sid": "4000017",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "幕墙",
                                    "is_show": 1,
                                    "sid": "4000018",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "建筑智能化",
                                    "is_show": 1,
                                    "sid": "4000019",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "电梯",
                                    "is_show": 1,
                                    "sid": "4000020",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "消防设施",
                                    "is_show": 1,
                                    "sid": "4000021",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "机电设备安装",
                                    "is_show": 1,
                                    "sid": "4000022",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "高耸构筑物",
                                    "is_show": 1,
                                    "sid": "4000023",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "建筑防水/防腐/保温",
                                    "is_show": 1,
                                    "sid": "4000024",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "仿古建筑及修缮",
                                    "is_show": 1,
                                    "sid": "4000025",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "广播/音响和会议系统",
                                    "is_show": 1,
                                    "sid": "4000026",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "大屏幕显示系统 ",
                                    "is_show": 1,
                                    "sid": "4000027",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "智能灯光",
                                    "is_show": 1,
                                    "sid": "4000028",
                                    "pid": "4000005",
                                    "list": []
                                },
                                {
                                    "name": "其他特种",
                                    "is_show": 1,
                                    "sid": "4000029",
                                    "pid": "4000005",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "市政工程",
                            "is_show": 1,
                            "sid": "4000030",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "道路",
                                    "is_show": 1,
                                    "sid": "4000031",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "桥梁",
                                    "is_show": 1,
                                    "sid": "4000032",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "隧道",
                                    "is_show": 1,
                                    "sid": "4000033",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "给水",
                                    "is_show": 1,
                                    "sid": "4000034",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "排水",
                                    "is_show": 1,
                                    "sid": "4000035",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "防洪堤防",
                                    "is_show": 1,
                                    "sid": "4000036",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "燃气",
                                    "is_show": 1,
                                    "sid": "4000037",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "热能及供热",
                                    "is_show": 1,
                                    "sid": "4000038",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "体育场地设施",
                                    "is_show": 1,
                                    "sid": "4000039",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "道路照明",
                                    "is_show": 1,
                                    "sid": "4000040",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "城市景观/户外广告",
                                    "is_show": 1,
                                    "sid": "4000041",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "垃圾处理",
                                    "is_show": 1,
                                    "sid": "4000042",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "市容环境综合整治",
                                    "is_show": 1,
                                    "sid": "4000043",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "综合管廊",
                                    "is_show": 1,
                                    "sid": "4000044",
                                    "pid": "4000030",
                                    "list": []
                                },
                                {
                                    "name": "城市公共广场",
                                    "is_show": 1,
                                    "sid": "4000045",
                                    "pid": "4000030",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "铁路工程",
                            "is_show": 1,
                            "sid": "4000046",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "地质",
                                    "is_show": 1,
                                    "sid": "4000047",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "路基",
                                    "is_show": 1,
                                    "sid": "4000048",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "桥梁",
                                    "is_show": 1,
                                    "sid": "4000049",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "隧道",
                                    "is_show": 1,
                                    "sid": "4000050",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "电气化",
                                    "is_show": 1,
                                    "sid": "4000051",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "铺架",
                                    "is_show": 1,
                                    "sid": "4000052",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "通信与信息",
                                    "is_show": 1,
                                    "sid": "4000053",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "信号",
                                    "is_show": 1,
                                    "sid": "4000054",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "给水排水",
                                    "is_show": 1,
                                    "sid": "4000055",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "站场",
                                    "is_show": 1,
                                    "sid": "4000056",
                                    "pid": "4000046",
                                    "list": []
                                },
                                {
                                    "name": "防灾监控",
                                    "is_show": 1,
                                    "sid": "4000057",
                                    "pid": "4000046",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "城市轨道交通",
                            "is_show": 1,
                            "sid": "4000058",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "路基",
                                    "is_show": 1,
                                    "sid": "4000059",
                                    "pid": "4000058",
                                    "list": []
                                },
                                {
                                    "name": "轨道",
                                    "is_show": 1,
                                    "sid": "4000060",
                                    "pid": "4000058",
                                    "list": []
                                },
                                {
                                    "name": "桥涵",
                                    "is_show": 1,
                                    "sid": "4000061",
                                    "pid": "4000058",
                                    "list": []
                                },
                                {
                                    "name": "隧道/地下结构",
                                    "is_show": 1,
                                    "sid": "4000062",
                                    "pid": "4000058",
                                    "list": []
                                },
                                {
                                    "name": "给水排水",
                                    "is_show": 1,
                                    "sid": "4000063",
                                    "pid": "4000058",
                                    "list": []
                                },
                                {
                                    "name": "供电",
                                    "is_show": 1,
                                    "sid": "4000064",
                                    "pid": "4000058",
                                    "list": []
                                },
                                {
                                    "name": "信号",
                                    "is_show": 1,
                                    "sid": "4000065",
                                    "pid": "4000058",
                                    "list": []
                                },
                                {
                                    "name": "通信",
                                    "is_show": 1,
                                    "sid": "4000066",
                                    "pid": "4000058",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "水利水电工程",
                            "is_show": 0,
                            "sid": "4000067",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "基础处理",
                                    "is_show": 0,
                                    "sid": "4000068",
                                    "pid": "4000067",
                                    "list": []
                                },
                                {
                                    "name": "水工建筑物",
                                    "is_show": 0,
                                    "sid": "4000069",
                                    "pid": "4000067",
                                    "list": []
                                },
                                {
                                    "name": "引水和灌溉",
                                    "is_show": 0,
                                    "sid": "4000070",
                                    "pid": "4000067",
                                    "list": []
                                },
                                {
                                    "name": "河道和堤防",
                                    "is_show": 0,
                                    "sid": "4000071",
                                    "pid": "4000067",
                                    "list": []
                                },
                                {
                                    "name": "金属设备及安装",
                                    "is_show": 0,
                                    "sid": "4000072",
                                    "pid": "4000067",
                                    "list": []
                                },
                                {
                                    "name": "水土保持",
                                    "is_show": 0,
                                    "sid": "4000073",
                                    "pid": "4000067",
                                    "list": []
                                },
                                {
                                    "name": "农田水利",
                                    "is_show": 0,
                                    "sid": "4000074",
                                    "pid": "4000067",
                                    "list": []
                                },
                                {
                                    "name": "安全监测",
                                    "is_show": 0,
                                    "sid": "4000075",
                                    "pid": "4000067",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "石油/化工",
                            "is_show": 1,
                            "sid": "4000076",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "石油化工",
                                    "is_show": 1,
                                    "sid": "4000077",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "油田",
                                    "is_show": 1,
                                    "sid": "4000078",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "气田",
                                    "is_show": 1,
                                    "sid": "4000079",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "气体处理",
                                    "is_show": 1,
                                    "sid": "4000080",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "原油",
                                    "is_show": 1,
                                    "sid": "4000081",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "成品油",
                                    "is_show": 1,
                                    "sid": "4000082",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "输油",
                                    "is_show": 1,
                                    "sid": "4000083",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "输气",
                                    "is_show": 1,
                                    "sid": "4000084",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "管道",
                                    "is_show": 1,
                                    "sid": "4000085",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "储罐",
                                    "is_show": 1,
                                    "sid": "4000086",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "储库",
                                    "is_show": 1,
                                    "sid": "4000087",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "油库",
                                    "is_show": 1,
                                    "sid": "4000088",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "储气",
                                    "is_show": 1,
                                    "sid": "4000089",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "天然气",
                                    "is_show": 1,
                                    "sid": "4000090",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "气库",
                                    "is_show": 1,
                                    "sid": "4000091",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "炼油",
                                    "is_show": 1,
                                    "sid": "4000092",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "脱硫",
                                    "is_show": 1,
                                    "sid": "4000093",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "催化",
                                    "is_show": 1,
                                    "sid": "4000094",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "煤化工（煤制）",
                                    "is_show": 1,
                                    "sid": "4000095",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "碱",
                                    "is_show": 1,
                                    "sid": "4000096",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "酸",
                                    "is_show": 1,
                                    "sid": "4000097",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "醇",
                                    "is_show": 1,
                                    "sid": "4000098",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "烯",
                                    "is_show": 1,
                                    "sid": "4000099",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "苯",
                                    "is_show": 1,
                                    "sid": "4000100",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "氨",
                                    "is_show": 1,
                                    "sid": "4000101",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "脂",
                                    "is_show": 1,
                                    "sid": "4000102",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "磷",
                                    "is_show": 1,
                                    "sid": "4000103",
                                    "pid": "4000076",
                                    "list": []
                                },
                                {
                                    "name": "烷",
                                    "is_show": 1,
                                    "sid": "4000104",
                                    "pid": "4000076",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "电子与智能化 ",
                            "is_show": 0,
                            "sid": "4000105",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "暗室",
                                    "is_show": 0,
                                    "sid": "4000106",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "洁净",
                                    "is_show": 0,
                                    "sid": "4000107",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "防微振",
                                    "is_show": 0,
                                    "sid": "4000108",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "屏蔽室",
                                    "is_show": 0,
                                    "sid": "4000109",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "防静电",
                                    "is_show": 0,
                                    "sid": "4000110",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "纯水",
                                    "is_show": 0,
                                    "sid": "4000111",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "废水",
                                    "is_show": 0,
                                    "sid": "4000112",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "废弃",
                                    "is_show": 0,
                                    "sid": "4000113",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "气体",
                                    "is_show": 0,
                                    "sid": "4000114",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "雷达",
                                    "is_show": 0,
                                    "sid": "4000115",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "导航",
                                    "is_show": 0,
                                    "sid": "4000116",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "天线",
                                    "is_show": 0,
                                    "sid": "4000117",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "网络",
                                    "is_show": 0,
                                    "sid": "4000118",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "监控",
                                    "is_show": 0,
                                    "sid": "4000119",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "自动",
                                    "is_show": 0,
                                    "sid": "4000120",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "智能化",
                                    "is_show": 0,
                                    "sid": "4000121",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "安全技术防范",
                                    "is_show": 0,
                                    "sid": "4000122",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "应急指挥",
                                    "is_show": 0,
                                    "sid": "4000123",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "射频",
                                    "is_show": 0,
                                    "sid": "4000124",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "智能卡",
                                    "is_show": 0,
                                    "sid": "4000125",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "收费系统",
                                    "is_show": 0,
                                    "sid": "4000126",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "数据中心",
                                    "is_show": 0,
                                    "sid": "4000127",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "机房",
                                    "is_show": 0,
                                    "sid": "4000128",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "智能化系统集成",
                                    "is_show": 0,
                                    "sid": "4000129",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "建筑设备",
                                    "is_show": 0,
                                    "sid": "4000130",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "计算机网络",
                                    "is_show": 0,
                                    "sid": "4000131",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "信息导引",
                                    "is_show": 0,
                                    "sid": "4000132",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "通讯系统",
                                    "is_show": 0,
                                    "sid": "4000133",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "卫星",
                                    "is_show": 0,
                                    "sid": "4000134",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "有线电视",
                                    "is_show": 0,
                                    "sid": "4000135",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "停车场",
                                    "is_show": 0,
                                    "sid": "4000136",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "综合布线",
                                    "is_show": 0,
                                    "sid": "4000137",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "广播",
                                    "is_show": 0,
                                    "sid": "4000138",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "会议",
                                    "is_show": 0,
                                    "sid": "4000139",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "大屏幕",
                                    "is_show": 0,
                                    "sid": "4000140",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "音响",
                                    "is_show": 0,
                                    "sid": "4000141",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "舞台",
                                    "is_show": 0,
                                    "sid": "4000142",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "火灾",
                                    "is_show": 0,
                                    "sid": "4000143",
                                    "pid": "4000105",
                                    "list": []
                                },
                                {
                                    "name": "消防",
                                    "is_show": 0,
                                    "sid": "4000144",
                                    "pid": "4000105",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "港口与航道",
                            "is_show": 0,
                            "sid": "4000145",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "码头",
                                    "is_show": 0,
                                    "sid": "4000146",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "港口",
                                    "is_show": 0,
                                    "sid": "4000147",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "地基处理",
                                    "is_show": 0,
                                    "sid": "4000148",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "防波堤",
                                    "is_show": 0,
                                    "sid": "4000149",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "护岸",
                                    "is_show": 0,
                                    "sid": "4000150",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "围堰",
                                    "is_show": 0,
                                    "sid": "4000151",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "堆场",
                                    "is_show": 0,
                                    "sid": "4000152",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "陆域",
                                    "is_show": 0,
                                    "sid": "4000153",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "筒仓",
                                    "is_show": 0,
                                    "sid": "4000154",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "船坞",
                                    "is_show": 0,
                                    "sid": "4000155",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "船台",
                                    "is_show": 0,
                                    "sid": "4000156",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "船闸",
                                    "is_show": 0,
                                    "sid": "4000157",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "船舶",
                                    "is_show": 0,
                                    "sid": "4000158",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "升船机",
                                    "is_show": 0,
                                    "sid": "4000159",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "地基",
                                    "is_show": 0,
                                    "sid": "4000160",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "土石方",
                                    "is_show": 0,
                                    "sid": "4000161",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "灯塔",
                                    "is_show": 0,
                                    "sid": "4000162",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "海岸",
                                    "is_show": 0,
                                    "sid": "4000163",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "海上风电",
                                    "is_show": 0,
                                    "sid": "4000164",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "清礁",
                                    "is_show": 0,
                                    "sid": "4000165",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "清淤",
                                    "is_show": 0,
                                    "sid": "4000166",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "炸礁",
                                    "is_show": 0,
                                    "sid": "4000167",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "水下开挖",
                                    "is_show": 0,
                                    "sid": "4000168",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "水下清障",
                                    "is_show": 0,
                                    "sid": "4000169",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "疏浚",
                                    "is_show": 0,
                                    "sid": "4000170",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "吹填",
                                    "is_show": 0,
                                    "sid": "4000171",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "航道",
                                    "is_show": 0,
                                    "sid": "4000172",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "港口与航道总承包",
                                    "is_show": 0,
                                    "sid": "4000173",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "航道专业承包",
                                    "is_show": 0,
                                    "sid": "4000174",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "港口与海岸专业承包",
                                    "is_show": 0,
                                    "sid": "4000175",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "港航设备安装及水上交管专业承包",
                                    "is_show": 0,
                                    "sid": "4000176",
                                    "pid": "4000145",
                                    "list": []
                                },
                                {
                                    "name": "通航建筑专业承包",
                                    "is_show": 0,
                                    "sid": "4000177",
                                    "pid": "4000145",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "冶金",
                            "is_show": 0,
                            "sid": "4000178",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "冶炼",
                                    "is_show": 0,
                                    "sid": "4000179",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "冶金",
                                    "is_show": 0,
                                    "sid": "4000180",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "有色金属",
                                    "is_show": 0,
                                    "sid": "4000181",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "金属材料",
                                    "is_show": 0,
                                    "sid": "4000182",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "焦化",
                                    "is_show": 0,
                                    "sid": "4000183",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "耐火材料",
                                    "is_show": 0,
                                    "sid": "4000184",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "矿",
                                    "is_show": 0,
                                    "sid": "4000185",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "选矿",
                                    "is_show": 0,
                                    "sid": "4000186",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "结构",
                                    "is_show": 0,
                                    "sid": "4000187",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "电气",
                                    "is_show": 0,
                                    "sid": "4000188",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "暖通",
                                    "is_show": 0,
                                    "sid": "4000189",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "给水",
                                    "is_show": 0,
                                    "sid": "4000190",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "排水",
                                    "is_show": 0,
                                    "sid": "4000191",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "动力",
                                    "is_show": 0,
                                    "sid": "4000192",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "测量",
                                    "is_show": 0,
                                    "sid": "4000193",
                                    "pid": "4000178",
                                    "list": []
                                },
                                {
                                    "name": "冶金施工总承包",
                                    "is_show": 0,
                                    "sid": "4000194",
                                    "pid": "4000178",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "矿山",
                            "is_show": 0,
                            "sid": "4000195",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "矿井",
                                    "is_show": 0,
                                    "sid": "4000196",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "露天矿",
                                    "is_show": 0,
                                    "sid": "4000197",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "洗矿",
                                    "is_show": 0,
                                    "sid": "4000198",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "选矿",
                                    "is_show": 0,
                                    "sid": "4000199",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "尾矿",
                                    "is_show": 0,
                                    "sid": "4000200",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "井下机电",
                                    "is_show": 0,
                                    "sid": "4000201",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "转载点",
                                    "is_show": 0,
                                    "sid": "4000202",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "原料仓",
                                    "is_show": 0,
                                    "sid": "4000203",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "产品仓",
                                    "is_show": 0,
                                    "sid": "4000204",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "装车仓",
                                    "is_show": 0,
                                    "sid": "4000205",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "栈桥",
                                    "is_show": 0,
                                    "sid": "4000206",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "配套",
                                    "is_show": 0,
                                    "sid": "4000207",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "铁路",
                                    "is_show": 0,
                                    "sid": "4000208",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "公路",
                                    "is_show": 0,
                                    "sid": "4000209",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "送变电",
                                    "is_show": 0,
                                    "sid": "4000210",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "通信",
                                    "is_show": 0,
                                    "sid": "4000211",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "环保",
                                    "is_show": 0,
                                    "sid": "4000212",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "绿化",
                                    "is_show": 0,
                                    "sid": "4000213",
                                    "pid": "4000195",
                                    "list": []
                                },
                                {
                                    "name": "采矿",
                                    "is_show": 0,
                                    "sid": "4000214",
                                    "pid": "4000195",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "通信",
                            "is_show": 1,
                            "sid": "4000215",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "通信",
                                    "is_show": 1,
                                    "sid": "4000216",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "通信线路",
                                    "is_show": 1,
                                    "sid": "4000217",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "传输设备",
                                    "is_show": 1,
                                    "sid": "4000218",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "交换",
                                    "is_show": 1,
                                    "sid": "4000219",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "数据及多媒体",
                                    "is_show": 1,
                                    "sid": "4000220",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "综合布线",
                                    "is_show": 1,
                                    "sid": "4000221",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "通信管道",
                                    "is_show": 1,
                                    "sid": "4000222",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "微波通信",
                                    "is_show": 1,
                                    "sid": "4000223",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "卫星地球站",
                                    "is_show": 1,
                                    "sid": "4000224",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "移动通信",
                                    "is_show": 1,
                                    "sid": "4000225",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "通信电源",
                                    "is_show": 1,
                                    "sid": "4000226",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "通信信息系统集成",
                                    "is_show": 1,
                                    "sid": "4000227",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "通信用户管线建设",
                                    "is_show": 1,
                                    "sid": "4000228",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "中国联通",
                                    "is_show": 1,
                                    "sid": "4000229",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "中国电信",
                                    "is_show": 1,
                                    "sid": "4000230",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "中国移动",
                                    "is_show": 1,
                                    "sid": "4000231",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "中国铁塔",
                                    "is_show": 1,
                                    "sid": "4000232",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "基站",
                                    "is_show": 1,
                                    "sid": "4000233",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "信息化",
                                    "is_show": 1,
                                    "sid": "4000234",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "调度",
                                    "is_show": 1,
                                    "sid": "4000235",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "通信管线",
                                    "is_show": 1,
                                    "sid": "4000236",
                                    "pid": "4000215",
                                    "list": []
                                },
                                {
                                    "name": "综合布线",
                                    "is_show": 1,
                                    "sid": "4000237",
                                    "pid": "4000215",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "电力",
                            "is_show": 1,
                            "sid": "4000238",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "火电安装",
                                    "is_show": 1,
                                    "sid": "4000239",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "核电安装",
                                    "is_show": 1,
                                    "sid": "4000240",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "输变电",
                                    "is_show": 1,
                                    "sid": "4000241",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "电力线路",
                                    "is_show": 1,
                                    "sid": "4000242",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "供电用电",
                                    "is_show": 1,
                                    "sid": "4000243",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "脱硫/脱硝 ",
                                    "is_show": 1,
                                    "sid": "4000244",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "电力调试",
                                    "is_show": 1,
                                    "sid": "4000245",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "风电",
                                    "is_show": 1,
                                    "sid": "4000246",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "太阳能发电",
                                    "is_show": 1,
                                    "sid": "4000247",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "生物质能利用",
                                    "is_show": 1,
                                    "sid": "4000248",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "承装修试",
                                    "is_show": 1,
                                    "sid": "4000249",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "其他新能源",
                                    "is_show": 1,
                                    "sid": "4000250",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "承装（修/试）电力设施",
                                    "is_show": 1,
                                    "sid": "4000251",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "水利水电工程施工总承包",
                                    "is_show": 1,
                                    "sid": "4000252",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "电力工程施工总承包",
                                    "is_show": 1,
                                    "sid": "4000253",
                                    "pid": "4000238",
                                    "list": []
                                },
                                {
                                    "name": "输变电工程专业承包",
                                    "is_show": 1,
                                    "sid": "4000254",
                                    "pid": "4000238",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "机场工程",
                            "is_show": 0,
                            "sid": "4000255",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "飞行区",
                                    "is_show": 0,
                                    "sid": "4000256",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "土石方",
                                    "is_show": 0,
                                    "sid": "4000257",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "地基处理",
                                    "is_show": 0,
                                    "sid": "4000258",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "机场",
                                    "is_show": 0,
                                    "sid": "4000259",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "道面",
                                    "is_show": 0,
                                    "sid": "4000260",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "排水",
                                    "is_show": 0,
                                    "sid": "4000261",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "桥梁",
                                    "is_show": 0,
                                    "sid": "4000262",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "涵隧",
                                    "is_show": 0,
                                    "sid": "4000263",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "消防管网",
                                    "is_show": 0,
                                    "sid": "4000264",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "管廊",
                                    "is_show": 0,
                                    "sid": "4000265",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "车道",
                                    "is_show": 0,
                                    "sid": "4000266",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "巡场路",
                                    "is_show": 0,
                                    "sid": "4000267",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "场道",
                                    "is_show": 0,
                                    "sid": "4000268",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "配套",
                                    "is_show": 0,
                                    "sid": "4000269",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "空管",
                                    "is_show": 0,
                                    "sid": "4000270",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "塔台",
                                    "is_show": 0,
                                    "sid": "4000271",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "通信",
                                    "is_show": 0,
                                    "sid": "4000272",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "转报",
                                    "is_show": 0,
                                    "sid": "4000273",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "地面站",
                                    "is_show": 0,
                                    "sid": "4000274",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "雷达",
                                    "is_show": 0,
                                    "sid": "4000275",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "监控",
                                    "is_show": 0,
                                    "sid": "4000276",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "着陆",
                                    "is_show": 0,
                                    "sid": "4000277",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "航线",
                                    "is_show": 0,
                                    "sid": "4000278",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "导航",
                                    "is_show": 0,
                                    "sid": "4000279",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "航行情报",
                                    "is_show": 0,
                                    "sid": "4000280",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "气象观测",
                                    "is_show": 0,
                                    "sid": "4000281",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "气象雷达",
                                    "is_show": 0,
                                    "sid": "4000282",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "防雷",
                                    "is_show": 0,
                                    "sid": "4000283",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "配电",
                                    "is_show": 0,
                                    "sid": "4000284",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "弱电",
                                    "is_show": 0,
                                    "sid": "4000285",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "航站楼",
                                    "is_show": 0,
                                    "sid": "4000286",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "货运区",
                                    "is_show": 0,
                                    "sid": "4000287",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "航班信息",
                                    "is_show": 0,
                                    "sid": "4000288",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "离岗控制",
                                    "is_show": 0,
                                    "sid": "4000289",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "引导",
                                    "is_show": 0,
                                    "sid": "4000290",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "安检",
                                    "is_show": 0,
                                    "sid": "4000291",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "行李",
                                    "is_show": 0,
                                    "sid": "4000292",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "值机",
                                    "is_show": 0,
                                    "sid": "4000293",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "登机门",
                                    "is_show": 0,
                                    "sid": "4000294",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "问询",
                                    "is_show": 0,
                                    "sid": "4000295",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "广播",
                                    "is_show": 0,
                                    "sid": "4000296",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "综合布线",
                                    "is_show": 0,
                                    "sid": "4000297",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "消防监控",
                                    "is_show": 0,
                                    "sid": "4000298",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "机房",
                                    "is_show": 0,
                                    "sid": "4000299",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "通讯",
                                    "is_show": 0,
                                    "sid": "4000300",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "助航",
                                    "is_show": 0,
                                    "sid": "4000301",
                                    "pid": "4000255",
                                    "list": []
                                },
                                {
                                    "name": "灯光系统",
                                    "is_show": 0,
                                    "sid": "4000302",
                                    "pid": "4000255",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "公路工程",
                            "is_show": 0,
                            "sid": "4000303",
                            "pid": "4000001",
                            "list": [
                                {
                                    "name": "新建",
                                    "is_show": 0,
                                    "sid": "4000304",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "改造",
                                    "is_show": 0,
                                    "sid": "4000305",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "拓宽",
                                    "is_show": 0,
                                    "sid": "4000306",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "养护",
                                    "is_show": 0,
                                    "sid": "4000307",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "高速",
                                    "is_show": 0,
                                    "sid": "4000308",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "省道",
                                    "is_show": 0,
                                    "sid": "4000309",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "国道",
                                    "is_show": 0,
                                    "sid": "4000310",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "县道",
                                    "is_show": 0,
                                    "sid": "4000311",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "乡道",
                                    "is_show": 0,
                                    "sid": "4000312",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "提升",
                                    "is_show": 0,
                                    "sid": "4000313",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "大修",
                                    "is_show": 0,
                                    "sid": "4000314",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "扩建",
                                    "is_show": 0,
                                    "sid": "4000315",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "中修",
                                    "is_show": 0,
                                    "sid": "4000316",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "危桥",
                                    "is_show": 0,
                                    "sid": "4000317",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "排水",
                                    "is_show": 0,
                                    "sid": "4000318",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "公路",
                                    "is_show": 0,
                                    "sid": "4000319",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "道路",
                                    "is_show": 0,
                                    "sid": "4000320",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "桥涵",
                                    "is_show": 0,
                                    "sid": "4000321",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "安全设施",
                                    "is_show": 0,
                                    "sid": "4000322",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "通信",
                                    "is_show": 0,
                                    "sid": "4000323",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "监控",
                                    "is_show": 0,
                                    "sid": "4000324",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "收费",
                                    "is_show": 0,
                                    "sid": "4000325",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "干线传输",
                                    "is_show": 0,
                                    "sid": "4000326",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "光缆敷设",
                                    "is_show": 0,
                                    "sid": "4000327",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "电缆敷设",
                                    "is_show": 0,
                                    "sid": "4000328",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "信息采集",
                                    "is_show": 0,
                                    "sid": "4000329",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "控制系统",
                                    "is_show": 0,
                                    "sid": "4000330",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "照明",
                                    "is_show": 0,
                                    "sid": "4000331",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "智能交通",
                                    "is_show": 0,
                                    "sid": "4000332",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "通信管道",
                                    "is_show": 0,
                                    "sid": "4000333",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "机电",
                                    "is_show": 0,
                                    "sid": "4000334",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "配套",
                                    "is_show": 0,
                                    "sid": "4000335",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "路面",
                                    "is_show": 0,
                                    "sid": "4000336",
                                    "pid": "4000303",
                                    "list": []
                                },
                                {
                                    "name": "路基",
                                    "is_show": 0,
                                    "sid": "4000337",
                                    "pid": "4000303",
                                    "list": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "货物类",
                    "is_show": 1,
                    "sid": "4000002",
                    "pid": "0",
                    "list": [
                        {
                            "name": "机械/设备",
                            "is_show": 1,
                            "sid": "4000338",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "建筑机械",
                                    "is_show": 1,
                                    "sid": "4000339",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "盾构设备",
                                            "is_show": 1,
                                            "sid": "4000340",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "挖掘机械",
                                            "is_show": 1,
                                            "sid": "4000341",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "桩工机械",
                                            "is_show": 1,
                                            "sid": "4000342",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "铲土运输机械",
                                            "is_show": 1,
                                            "sid": "4000343",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "压实与路面机械",
                                            "is_show": 1,
                                            "sid": "4000344",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "塔吊",
                                            "is_show": 1,
                                            "sid": "4000345",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "混凝土机械",
                                            "is_show": 1,
                                            "sid": "4000346",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "凿岩机械",
                                            "is_show": 1,
                                            "sid": "4000347",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "桥梁施工机械",
                                            "is_show": 1,
                                            "sid": "4000348",
                                            "pid": "4000339",
                                            "list": []
                                        },
                                        {
                                            "name": "公路养护设备",
                                            "is_show": 0,
                                            "sid": "4000349",
                                            "pid": "4000339",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "城市轨道工程设备",
                                    "is_show": 0,
                                    "sid": "4000350",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "通风设备",
                                            "is_show": 0,
                                            "sid": "4000351",
                                            "pid": "4000350",
                                            "list": []
                                        },
                                        {
                                            "name": "自动售检票",
                                            "is_show": 0,
                                            "sid": "4000352",
                                            "pid": "4000350",
                                            "list": []
                                        },
                                        {
                                            "name": "防灾报警设备及消防",
                                            "is_show": 0,
                                            "sid": "4000353",
                                            "pid": "4000350",
                                            "list": []
                                        },
                                        {
                                            "name": "屏蔽门设备",
                                            "is_show": 0,
                                            "sid": "4000354",
                                            "pid": "4000350",
                                            "list": []
                                        },
                                        {
                                            "name": "综合监控设备",
                                            "is_show": 0,
                                            "sid": "4000355",
                                            "pid": "4000350",
                                            "list": []
                                        },
                                        {
                                            "name": "车辆段设备",
                                            "is_show": 0,
                                            "sid": "4000356",
                                            "pid": "4000350",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "民航设备",
                                    "is_show": 0,
                                    "sid": "4000357",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "旅客登机桥",
                                            "is_show": 0,
                                            "sid": "4000358",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "机场目视助航",
                                            "is_show": 0,
                                            "sid": "4000359",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "机场供电设备",
                                            "is_show": 0,
                                            "sid": "4000360",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "机场弱电设备",
                                            "is_show": 0,
                                            "sid": "4000361",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "空管通信",
                                            "is_show": 0,
                                            "sid": "4000362",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "空管导航设备",
                                            "is_show": 0,
                                            "sid": "4000363",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "空管自动化",
                                            "is_show": 0,
                                            "sid": "4000364",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "空管雷达",
                                            "is_show": 0,
                                            "sid": "4000365",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "空管气象",
                                            "is_show": 0,
                                            "sid": "4000366",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "机场供油",
                                            "is_show": 0,
                                            "sid": "4000367",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "行李处理系统",
                                            "is_show": 0,
                                            "sid": "4000368",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "航空配餐系统设备",
                                            "is_show": 0,
                                            "sid": "4000369",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "机场应急救援设备",
                                            "is_show": 0,
                                            "sid": "4000370",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "旅客引导标识",
                                            "is_show": 0,
                                            "sid": "4000371",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "航空货运站",
                                            "is_show": 0,
                                            "sid": "4000372",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "飞机泊位引导系统",
                                            "is_show": 0,
                                            "sid": "4000373",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "机场安检设备",
                                            "is_show": 0,
                                            "sid": "4000374",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "安检探测成像设备",
                                            "is_show": 0,
                                            "sid": "4000375",
                                            "pid": "4000357",
                                            "list": []
                                        },
                                        {
                                            "name": "安检物质探测设备",
                                            "is_show": 0,
                                            "sid": "4000376",
                                            "pid": "4000357",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "矿山机械",
                                    "is_show": 0,
                                    "sid": "4000377",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "井下采掘机械",
                                            "is_show": 0,
                                            "sid": "4000378",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "矿井提升运输设备",
                                            "is_show": 0,
                                            "sid": "4000379",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "矿井支护",
                                            "is_show": 0,
                                            "sid": "4000380",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "粉碎机械",
                                            "is_show": 0,
                                            "sid": "4000381",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "研磨设备",
                                            "is_show": 0,
                                            "sid": "4000382",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "洗选设备",
                                            "is_show": 0,
                                            "sid": "4000383",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "脱水设备",
                                            "is_show": 0,
                                            "sid": "4000384",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "烧结设备",
                                            "is_show": 0,
                                            "sid": "4000385",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "成型设备",
                                            "is_show": 0,
                                            "sid": "4000386",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "勘探设备",
                                            "is_show": 0,
                                            "sid": "4000387",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "检测设备",
                                            "is_show": 0,
                                            "sid": "4000388",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "运输车辆 矿山",
                                            "is_show": 0,
                                            "sid": "4000389",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "运输车辆 煤矿",
                                            "is_show": 0,
                                            "sid": "4000390",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "其他辅助设备 矿山",
                                            "is_show": 0,
                                            "sid": "4000391",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "井下采掘/提升成套设备",
                                            "is_show": 0,
                                            "sid": "4000392",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "露天矿设备",
                                            "is_show": 0,
                                            "sid": "4000393",
                                            "pid": "4000377",
                                            "list": []
                                        },
                                        {
                                            "name": "洗煤设备",
                                            "is_show": 0,
                                            "sid": "4000394",
                                            "pid": "4000377",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "石油/天然气设备",
                                    "is_show": 0,
                                    "sid": "4000395",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "石油/天然气勘探和钻采设备",
                                            "is_show": 0,
                                            "sid": "4000396",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "石油钻采设备",
                                            "is_show": 0,
                                            "sid": "4000397",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "天然气勘探设备",
                                            "is_show": 0,
                                            "sid": "4000398",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "天然气钻采设备",
                                            "is_show": 0,
                                            "sid": "4000399",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "石油集输",
                                            "is_show": 0,
                                            "sid": "4000400",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "石油储运",
                                            "is_show": 0,
                                            "sid": "4000401",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "天然气集输",
                                            "is_show": 0,
                                            "sid": "4000402",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "天然气储运",
                                            "is_show": 0,
                                            "sid": "4000403",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "石油/天然气集输与储运",
                                            "is_show": 0,
                                            "sid": "4000404",
                                            "pid": "4000395",
                                            "list": []
                                        },
                                        {
                                            "name": "炼油设备",
                                            "is_show": 0,
                                            "sid": "4000405",
                                            "pid": "4000395",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "冶金机械",
                                    "is_show": 0,
                                    "sid": "4000406",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "黑色金属原料备制及冶炼设备",
                                            "is_show": 0,
                                            "sid": "4000407",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "有色金属原料备制及冶炼设备",
                                            "is_show": 0,
                                            "sid": "4000408",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "冶炼设备",
                                            "is_show": 0,
                                            "sid": "4000409",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "金属轧制设备",
                                            "is_show": 0,
                                            "sid": "4000410",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "压延设备",
                                            "is_show": 0,
                                            "sid": "4000411",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "坯连铸机",
                                            "is_show": 0,
                                            "sid": "4000412",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "冷连轧机",
                                            "is_show": 0,
                                            "sid": "4000413",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "黑色金属轧制设备",
                                            "is_show": 0,
                                            "sid": "4000414",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "有色金属压延设备",
                                            "is_show": 0,
                                            "sid": "4000415",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "大型宽厚板坯连铸机成套设备",
                                            "is_show": 0,
                                            "sid": "4000416",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "大型热连轧板机成套设备",
                                            "is_show": 0,
                                            "sid": "4000417",
                                            "pid": "4000406",
                                            "list": []
                                        },
                                        {
                                            "name": "大型板带冷连轧机成套设备",
                                            "is_show": 0,
                                            "sid": "4000418",
                                            "pid": "4000406",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "化工机械",
                                    "is_show": 0,
                                    "sid": "4000419",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "化工装置",
                                            "is_show": 0,
                                            "sid": "4000420",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "橡胶与塑料加工机械",
                                            "is_show": 0,
                                            "sid": "4000421",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "制药设备",
                                            "is_show": 0,
                                            "sid": "4000422",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "中药炮制设备",
                                            "is_show": 0,
                                            "sid": "4000423",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "制碱项目主要设备",
                                            "is_show": 0,
                                            "sid": "4000424",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "制盐项目主要设备",
                                            "is_show": 0,
                                            "sid": "4000425",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "压力容器",
                                            "is_show": 0,
                                            "sid": "4000426",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "化工装备",
                                            "is_show": 0,
                                            "sid": "4000427",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "橡胶加工",
                                            "is_show": 0,
                                            "sid": "4000428",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "塑料加工",
                                            "is_show": 0,
                                            "sid": "4000429",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "制碱设备",
                                            "is_show": 0,
                                            "sid": "4000430",
                                            "pid": "4000419",
                                            "list": []
                                        },
                                        {
                                            "name": "制盐设备",
                                            "is_show": 0,
                                            "sid": "4000431",
                                            "pid": "4000419",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "煤化工设备",
                                    "is_show": 0,
                                    "sid": "4000432",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "煤粉/煤浆加工设备",
                                            "is_show": 0,
                                            "sid": "4000433",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "煤气化设备",
                                            "is_show": 0,
                                            "sid": "4000434",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "传质设备",
                                            "is_show": 0,
                                            "sid": "4000435",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "反应设备",
                                            "is_show": 0,
                                            "sid": "4000436",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "浓缩设备",
                                            "is_show": 0,
                                            "sid": "4000437",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "传热设备",
                                            "is_show": 0,
                                            "sid": "4000438",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "储运设备",
                                            "is_show": 0,
                                            "sid": "4000439",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "输送设备",
                                            "is_show": 0,
                                            "sid": "4000440",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "输送设备 化工",
                                            "is_show": 0,
                                            "sid": "4000441",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "加工设备 化工",
                                            "is_show": 0,
                                            "sid": "4000442",
                                            "pid": "4000432",
                                            "list": []
                                        },
                                        {
                                            "name": "储运设备 化工",
                                            "is_show": 0,
                                            "sid": "4000443",
                                            "pid": "4000432",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "轻工机械",
                                    "is_show": 0,
                                    "sid": "4000444",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "制浆造纸纸制品装备",
                                            "is_show": 0,
                                            "sid": "4000445",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "酒/饮料加工及罐装设备",
                                            "is_show": 0,
                                            "sid": "4000446",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "乳品加工设备",
                                            "is_show": 0,
                                            "sid": "4000447",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "制糖设备",
                                            "is_show": 0,
                                            "sid": "4000448",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "制盐设备",
                                            "is_show": 0,
                                            "sid": "4000449",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "制革工艺与皮革加工设备",
                                            "is_show": 0,
                                            "sid": "4000450",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "制鞋设备",
                                            "is_show": 0,
                                            "sid": "4000451",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "钟表生产设备",
                                            "is_show": 0,
                                            "sid": "4000452",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "自行车生产设备",
                                            "is_show": 0,
                                            "sid": "4000453",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "电光源制造设备",
                                            "is_show": 0,
                                            "sid": "4000454",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "缝纫与服饰加工设备",
                                            "is_show": 0,
                                            "sid": "4000455",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "日用化工设备",
                                            "is_show": 0,
                                            "sid": "4000456",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "日用电器设备",
                                            "is_show": 0,
                                            "sid": "4000457",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "厨房设备",
                                            "is_show": 0,
                                            "sid": "4000458",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "屠宰及肉类加工设备",
                                            "is_show": 0,
                                            "sid": "4000459",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "食品冷冻保鲜设备",
                                            "is_show": 0,
                                            "sid": "4000460",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "烟草加工设备",
                                            "is_show": 0,
                                            "sid": "4000461",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "木工家具加工设备",
                                            "is_show": 0,
                                            "sid": "4000462",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "玻璃制造与加工设备",
                                            "is_show": 0,
                                            "sid": "4000463",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "陶瓷制造与加工设备",
                                            "is_show": 0,
                                            "sid": "4000464",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "洗涤设备",
                                            "is_show": 0,
                                            "sid": "4000465",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "造纸设备",
                                            "is_show": 0,
                                            "sid": "4000466",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "罐装设备",
                                            "is_show": 0,
                                            "sid": "4000467",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "乳品加工",
                                            "is_show": 0,
                                            "sid": "4000468",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "皮革加工设备",
                                            "is_show": 0,
                                            "sid": "4000469",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "服饰加工设备",
                                            "is_show": 0,
                                            "sid": "4000470",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "肉类加工设备",
                                            "is_show": 0,
                                            "sid": "4000471",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "玻璃制造",
                                            "is_show": 0,
                                            "sid": "4000472",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "玻璃加工",
                                            "is_show": 0,
                                            "sid": "4000473",
                                            "pid": "4000444",
                                            "list": []
                                        },
                                        {
                                            "name": "陶瓷加工",
                                            "is_show": 0,
                                            "sid": "4000474",
                                            "pid": "4000444",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "农业机械",
                                    "is_show": 0,
                                    "sid": "4000475",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "耕整地机械",
                                            "is_show": 0,
                                            "sid": "4000476",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "种植施肥机械",
                                            "is_show": 0,
                                            "sid": "4000477",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "田间管理机械",
                                            "is_show": 0,
                                            "sid": "4000478",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "收获机械",
                                            "is_show": 0,
                                            "sid": "4000479",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "收获后处理机械",
                                            "is_show": 0,
                                            "sid": "4000480",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "农产品初加工机械",
                                            "is_show": 0,
                                            "sid": "4000481",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "农用搬运机械",
                                            "is_show": 0,
                                            "sid": "4000482",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "排灌机械",
                                            "is_show": 0,
                                            "sid": "4000483",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "畜牧水产养殖机械",
                                            "is_show": 0,
                                            "sid": "4000484",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "动力机械",
                                            "is_show": 0,
                                            "sid": "4000485",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "农村可再生能源利用设备",
                                            "is_show": 0,
                                            "sid": "4000486",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "农田基本建设机械",
                                            "is_show": 0,
                                            "sid": "4000487",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "设施农业设备",
                                            "is_show": 0,
                                            "sid": "4000488",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "农业科研试验检测仪器设备",
                                            "is_show": 0,
                                            "sid": "4000489",
                                            "pid": "4000475",
                                            "list": []
                                        },
                                        {
                                            "name": "其他机械 农业",
                                            "is_show": 0,
                                            "sid": "4000490",
                                            "pid": "4000475",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "林业机械",
                                    "is_show": 0,
                                    "sid": "4000491",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "营林机械",
                                            "is_show": 0,
                                            "sid": "4000492",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "木材加工机械",
                                            "is_show": 0,
                                            "sid": "4000493",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "木材干燥机械",
                                            "is_show": 0,
                                            "sid": "4000494",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "林产化工机械",
                                            "is_show": 0,
                                            "sid": "4000495",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "种苗机械",
                                            "is_show": 0,
                                            "sid": "4000496",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "园林机械",
                                            "is_show": 0,
                                            "sid": "4000497",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "林副特产加工机械",
                                            "is_show": 0,
                                            "sid": "4000498",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "特产加工 设备",
                                            "is_show": 0,
                                            "sid": "4000499",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "森林消防 机械",
                                            "is_show": 0,
                                            "sid": "4000500",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "有害生物防治机械",
                                            "is_show": 0,
                                            "sid": "4000501",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "森林/湿地/荒漠化及野生动物检测设备",
                                            "is_show": 0,
                                            "sid": "4000502",
                                            "pid": "4000491",
                                            "list": []
                                        },
                                        {
                                            "name": "采伐运输",
                                            "is_show": 0,
                                            "sid": "4000503",
                                            "pid": "4000491",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "电子元器件及专用设备",
                                    "is_show": 0,
                                    "sid": "4000504",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "电子元件",
                                            "is_show": 0,
                                            "sid": "4000505",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "电子器件",
                                            "is_show": 0,
                                            "sid": "4000506",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "集成电路及为电子组件",
                                            "is_show": 0,
                                            "sid": "4000507",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "机电一体化自动控制",
                                            "is_show": 0,
                                            "sid": "4000508",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "半导体材料及制造设备",
                                            "is_show": 0,
                                            "sid": "4000509",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "光电器件及制造设备",
                                            "is_show": 0,
                                            "sid": "4000510",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "精密测量仪器",
                                            "is_show": 0,
                                            "sid": "4000511",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "自动化仪表",
                                            "is_show": 0,
                                            "sid": "4000512",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "电子加速器",
                                            "is_show": 0,
                                            "sid": "4000513",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "通讯网络设备",
                                            "is_show": 0,
                                            "sid": "4000514",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "机电一体化 自动控制",
                                            "is_show": 0,
                                            "sid": "4000515",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "集成电路及为电子组件",
                                            "is_show": 0,
                                            "sid": "4000516",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "半导体材料制造",
                                            "is_show": 0,
                                            "sid": "4000517",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "集成电路",
                                            "is_show": 0,
                                            "sid": "4000518",
                                            "pid": "4000504",
                                            "list": []
                                        },
                                        {
                                            "name": "其他专用电子设备及仪器",
                                            "is_show": 0,
                                            "sid": "4000519",
                                            "pid": "4000504",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "通信设备",
                                    "is_show": 1,
                                    "sid": "4000520",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "传输设备",
                                            "is_show": 1,
                                            "sid": "4000521",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "交换设备",
                                            "is_show": 1,
                                            "sid": "4000522",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "数据及多媒体设备",
                                            "is_show": 1,
                                            "sid": "4000523",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "微波通信设备",
                                            "is_show": 1,
                                            "sid": "4000524",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "卫星通信设备",
                                            "is_show": 1,
                                            "sid": "4000525",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "移动通信设备",
                                            "is_show": 1,
                                            "sid": "4000526",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "通信电源设备",
                                            "is_show": 1,
                                            "sid": "4000527",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "通信终端",
                                            "is_show": 1,
                                            "sid": "4000528",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "通信光缆/电缆",
                                            "is_show": 1,
                                            "sid": "4000529",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "通信光缆",
                                            "is_show": 1,
                                            "sid": "4000530",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "通信电缆",
                                            "is_show": 1,
                                            "sid": "4000531",
                                            "pid": "4000520",
                                            "list": []
                                        },
                                        {
                                            "name": "通信网络设备",
                                            "is_show": 1,
                                            "sid": "4000532",
                                            "pid": "4000520",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "广播/影视/舞台设备",
                                    "is_show": 0,
                                    "sid": "4000533",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "广播电视发射与传输设备",
                                            "is_show": 0,
                                            "sid": "4000534",
                                            "pid": "4000533",
                                            "list": []
                                        },
                                        {
                                            "name": "广播电视发射设备",
                                            "is_show": 0,
                                            "sid": "4000535",
                                            "pid": "4000533",
                                            "list": []
                                        },
                                        {
                                            "name": "广播电视 传输设备",
                                            "is_show": 0,
                                            "sid": "4000536",
                                            "pid": "4000533",
                                            "list": []
                                        },
                                        {
                                            "name": "音视频与图像技术设备",
                                            "is_show": 0,
                                            "sid": "4000537",
                                            "pid": "4000533",
                                            "list": []
                                        },
                                        {
                                            "name": "广播电视配套设备",
                                            "is_show": 0,
                                            "sid": "4000538",
                                            "pid": "4000533",
                                            "list": []
                                        },
                                        {
                                            "name": "电影设备",
                                            "is_show": 0,
                                            "sid": "4000539",
                                            "pid": "4000533",
                                            "list": []
                                        },
                                        {
                                            "name": "灯光/音响/舞台设备",
                                            "is_show": 0,
                                            "sid": "4000540",
                                            "pid": "4000533",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "海洋设备",
                                    "is_show": 0,
                                    "sid": "4000541",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "海洋环境监测设备及器械",
                                            "is_show": 0,
                                            "sid": "4000542",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋环境观测设备及器械",
                                            "is_show": 0,
                                            "sid": "4000543",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋环境分析仪器",
                                            "is_show": 0,
                                            "sid": "4000544",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋环境监测设备",
                                            "is_show": 0,
                                            "sid": "4000545",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋环境观测",
                                            "is_show": 0,
                                            "sid": "4000546",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋环境分析仪器",
                                            "is_show": 0,
                                            "sid": "4000547",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋调查设备及器械",
                                            "is_show": 0,
                                            "sid": "4000548",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋调查设备",
                                            "is_show": 0,
                                            "sid": "4000549",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海洋生物制药设备",
                                            "is_show": 0,
                                            "sid": "4000550",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海水利用设备",
                                            "is_show": 0,
                                            "sid": "4000551",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "海水淡化设备",
                                            "is_show": 0,
                                            "sid": "4000552",
                                            "pid": "4000541",
                                            "list": []
                                        },
                                        {
                                            "name": "其他海洋工程设备及器械",
                                            "is_show": 0,
                                            "sid": "4000553",
                                            "pid": "4000541",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "金属加工机械",
                                    "is_show": 0,
                                    "sid": "4000554",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "数控机床和加工中心设备",
                                            "is_show": 0,
                                            "sid": "4000555",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "金属切削机床",
                                            "is_show": 0,
                                            "sid": "4000556",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "锻压与锻压机械",
                                            "is_show": 0,
                                            "sid": "4000557",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "铸造与铸造设备",
                                            "is_show": 0,
                                            "sid": "4000558",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "焊接与焊接/切割设备",
                                            "is_show": 0,
                                            "sid": "4000559",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "切割设备",
                                            "is_show": 0,
                                            "sid": "4000560",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "焊接设备",
                                            "is_show": 0,
                                            "sid": "4000561",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "模具",
                                            "is_show": 0,
                                            "sid": "4000562",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "表面处理",
                                            "is_show": 0,
                                            "sid": "4000563",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "热处理设备",
                                            "is_show": 0,
                                            "sid": "4000564",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "数控机床",
                                            "is_show": 0,
                                            "sid": "4000565",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "锻压与锻压机械",
                                            "is_show": 0,
                                            "sid": "4000566",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "锻压机床",
                                            "is_show": 0,
                                            "sid": "4000567",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "铸造机",
                                            "is_show": 0,
                                            "sid": "4000568",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "铸造设备",
                                            "is_show": 0,
                                            "sid": "4000569",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "理化检测设备",
                                            "is_show": 0,
                                            "sid": "4000570",
                                            "pid": "4000554",
                                            "list": []
                                        },
                                        {
                                            "name": "机电一体化",
                                            "is_show": 0,
                                            "sid": "4000571",
                                            "pid": "4000554",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "锅炉",
                                    "is_show": 0,
                                    "sid": "4000572",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "电站锅炉及辅机",
                                            "is_show": 0,
                                            "sid": "4000573",
                                            "pid": "4000572",
                                            "list": []
                                        },
                                        {
                                            "name": "工业锅炉及辅机",
                                            "is_show": 0,
                                            "sid": "4000574",
                                            "pid": "4000572",
                                            "list": []
                                        },
                                        {
                                            "name": "船用锅炉",
                                            "is_show": 0,
                                            "sid": "4000575",
                                            "pid": "4000572",
                                            "list": []
                                        },
                                        {
                                            "name": "机车锅炉",
                                            "is_show": 0,
                                            "sid": "4000576",
                                            "pid": "4000572",
                                            "list": []
                                        },
                                        {
                                            "name": "电站锅炉",
                                            "is_show": 0,
                                            "sid": "4000577",
                                            "pid": "4000572",
                                            "list": []
                                        },
                                        {
                                            "name": "工业锅炉",
                                            "is_show": 0,
                                            "sid": "4000578",
                                            "pid": "4000572",
                                            "list": []
                                        },
                                        {
                                            "name": "注汽锅炉",
                                            "is_show": 0,
                                            "sid": "4000579",
                                            "pid": "4000572",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "造纸机械",
                                    "is_show": 0,
                                    "sid": "4000580",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "制浆设备",
                                            "is_show": 0,
                                            "sid": "4000581",
                                            "pid": "4000580",
                                            "list": []
                                        },
                                        {
                                            "name": "造纸机",
                                            "is_show": 0,
                                            "sid": "4000582",
                                            "pid": "4000580",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "起重运输机械",
                                    "is_show": 0,
                                    "sid": "4000583",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "起重机械",
                                            "is_show": 0,
                                            "sid": "4000584",
                                            "pid": "4000583",
                                            "list": []
                                        },
                                        {
                                            "name": "输送机械",
                                            "is_show": 0,
                                            "sid": "4000585",
                                            "pid": "4000583",
                                            "list": []
                                        },
                                        {
                                            "name": "扶梯",
                                            "is_show": 0,
                                            "sid": "4000586",
                                            "pid": "4000583",
                                            "list": []
                                        },
                                        {
                                            "name": "电梯",
                                            "is_show": 0,
                                            "sid": "4000587",
                                            "pid": "4000583",
                                            "list": []
                                        },
                                        {
                                            "name": "装卸机械",
                                            "is_show": 0,
                                            "sid": "4000588",
                                            "pid": "4000583",
                                            "list": []
                                        },
                                        {
                                            "name": "扶梯与电梯",
                                            "is_show": 0,
                                            "sid": "4000589",
                                            "pid": "4000583",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "纺织机械",
                                    "is_show": 0,
                                    "sid": "4000590",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "棉纺前机械",
                                            "is_show": 0,
                                            "sid": "4000591",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "毛纺前机械",
                                            "is_show": 0,
                                            "sid": "4000592",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "纺纱机械",
                                            "is_show": 0,
                                            "sid": "4000593",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "络并捻机械",
                                            "is_show": 0,
                                            "sid": "4000594",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "织造机械",
                                            "is_show": 0,
                                            "sid": "4000595",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "针织机械",
                                            "is_show": 0,
                                            "sid": "4000596",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "非织造布机械",
                                            "is_show": 0,
                                            "sid": "4000597",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "印染整理机械",
                                            "is_show": 0,
                                            "sid": "4000598",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "化纤机械",
                                            "is_show": 0,
                                            "sid": "4000599",
                                            "pid": "4000590",
                                            "list": []
                                        },
                                        {
                                            "name": "纺织测试仪器",
                                            "is_show": 0,
                                            "sid": "4000600",
                                            "pid": "4000590",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "包装设备",
                                    "is_show": 0,
                                    "sid": "4000601",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "食品包装机械",
                                            "is_show": 0,
                                            "sid": "4000602",
                                            "pid": "4000601",
                                            "list": []
                                        },
                                        {
                                            "name": "药品专用包装机械",
                                            "is_show": 0,
                                            "sid": "4000603",
                                            "pid": "4000601",
                                            "list": []
                                        },
                                        {
                                            "name": "其它货物包装机械设备",
                                            "is_show": 0,
                                            "sid": "4000604",
                                            "pid": "4000601",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "生物制造设备",
                                    "is_show": 0,
                                    "sid": "4000605",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "发酵设备",
                                            "is_show": 0,
                                            "sid": "4000606",
                                            "pid": "4000605",
                                            "list": []
                                        },
                                        {
                                            "name": "生物质能设备",
                                            "is_show": 0,
                                            "sid": "4000607",
                                            "pid": "4000605",
                                            "list": []
                                        },
                                        {
                                            "name": "生物质能",
                                            "is_show": 0,
                                            "sid": "4000608",
                                            "pid": "4000605",
                                            "list": []
                                        },
                                        {
                                            "name": "生物制品加工设备",
                                            "is_show": 0,
                                            "sid": "4000609",
                                            "pid": "4000605",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "粮油食品加工机械",
                                    "is_show": 0,
                                    "sid": "4000610",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "粮食机械",
                                            "is_show": 0,
                                            "sid": "4000611",
                                            "pid": "4000610",
                                            "list": []
                                        },
                                        {
                                            "name": "油料加工机械",
                                            "is_show": 0,
                                            "sid": "4000612",
                                            "pid": "4000610",
                                            "list": []
                                        },
                                        {
                                            "name": "油料加工设备",
                                            "is_show": 0,
                                            "sid": "4000613",
                                            "pid": "4000610",
                                            "list": []
                                        },
                                        {
                                            "name": "食品加工设备",
                                            "is_show": 0,
                                            "sid": "4000614",
                                            "pid": "4000610",
                                            "list": []
                                        },
                                        {
                                            "name": "食品加工机械",
                                            "is_show": 0,
                                            "sid": "4000615",
                                            "pid": "4000610",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "非金属矿物制品工业专用设备",
                                    "is_show": 0,
                                    "sid": "4000616",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "水泥生产设备",
                                            "is_show": 0,
                                            "sid": "4000617",
                                            "pid": "4000616",
                                            "list": []
                                        },
                                        {
                                            "name": "玻璃加工制造设备",
                                            "is_show": 0,
                                            "sid": "4000618",
                                            "pid": "4000616",
                                            "list": []
                                        },
                                        {
                                            "name": "墙体材料制造设备",
                                            "is_show": 0,
                                            "sid": "4000619",
                                            "pid": "4000616",
                                            "list": []
                                        },
                                        {
                                            "name": "炉/窑",
                                            "is_show": 0,
                                            "sid": "4000620",
                                            "pid": "4000616",
                                            "list": []
                                        },
                                        {
                                            "name": "硅材料",
                                            "is_show": 0,
                                            "sid": "4000621",
                                            "pid": "4000616",
                                            "list": []
                                        },
                                        {
                                            "name": "石材切割加工设备",
                                            "is_show": 0,
                                            "sid": "4000622",
                                            "pid": "4000616",
                                            "list": []
                                        },
                                        {
                                            "name": "非金属矿物超细加工及改性设备",
                                            "is_show": 0,
                                            "sid": "4000623",
                                            "pid": "4000616",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "车辆",
                                    "is_show": 0,
                                    "sid": "4000624",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "矿山运输车辆",
                                            "is_show": 0,
                                            "sid": "4000625",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "小型轿车",
                                            "is_show": 0,
                                            "sid": "4000626",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "大中型客车",
                                            "is_show": 0,
                                            "sid": "4000627",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "载重车辆",
                                            "is_show": 0,
                                            "sid": "4000628",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "内燃机车",
                                            "is_show": 0,
                                            "sid": "4000629",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "电力机车",
                                            "is_show": 0,
                                            "sid": "4000630",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "工矿电机车",
                                            "is_show": 0,
                                            "sid": "4000631",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "铁路机务/车辆及动车组设备",
                                            "is_show": 0,
                                            "sid": "4000632",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "动车组设备",
                                            "is_show": 0,
                                            "sid": "4000633",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "铁路机务",
                                            "is_show": 0,
                                            "sid": "4000634",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "铁路车辆",
                                            "is_show": 0,
                                            "sid": "4000635",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "城市轨道车辆",
                                            "is_show": 0,
                                            "sid": "4000636",
                                            "pid": "4000624",
                                            "list": []
                                        },
                                        {
                                            "name": "摩托车",
                                            "is_show": 0,
                                            "sid": "4000637",
                                            "pid": "4000624",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "船舶设备",
                                    "is_show": 0,
                                    "sid": "4000638",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "船舶主动力装置",
                                            "is_show": 0,
                                            "sid": "4000639",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶辅助动力装置",
                                            "is_show": 0,
                                            "sid": "4000640",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶蒸汽锅炉及压缩空气装置",
                                            "is_show": 0,
                                            "sid": "4000641",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船用泵和管路系统",
                                            "is_show": 0,
                                            "sid": "4000642",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船用泵",
                                            "is_show": 0,
                                            "sid": "4000643",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶操纵",
                                            "is_show": 0,
                                            "sid": "4000644",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶推进",
                                            "is_show": 0,
                                            "sid": "4000645",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "造水机",
                                            "is_show": 0,
                                            "sid": "4000646",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶操纵设备",
                                            "is_show": 0,
                                            "sid": "4000647",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶自动化系统",
                                            "is_show": 0,
                                            "sid": "4000648",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船厂专用装焊设备",
                                            "is_show": 0,
                                            "sid": "4000649",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船厂专用切割设备",
                                            "is_show": 0,
                                            "sid": "4000650",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船厂专用流水线设备",
                                            "is_show": 0,
                                            "sid": "4000651",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船厂起重运输设备",
                                            "is_show": 0,
                                            "sid": "4000652",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "甲板机械",
                                            "is_show": 0,
                                            "sid": "4000653",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "舱室机械",
                                            "is_show": 0,
                                            "sid": "4000654",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶推进装置",
                                            "is_show": 0,
                                            "sid": "4000655",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "自动导航设备",
                                            "is_show": 0,
                                            "sid": "4000656",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶设计试验专用软硬件设备",
                                            "is_show": 0,
                                            "sid": "4000657",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶设计软件",
                                            "is_show": 0,
                                            "sid": "4000658",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶涂装设备",
                                            "is_show": 0,
                                            "sid": "4000659",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "船舶试验设备",
                                            "is_show": 0,
                                            "sid": "4000660",
                                            "pid": "4000638",
                                            "list": []
                                        },
                                        {
                                            "name": "其他专用设备",
                                            "is_show": 0,
                                            "sid": "4000661",
                                            "pid": "4000638",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "航空航天设备",
                                    "is_show": 0,
                                    "sid": "4000662",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "飞机采购",
                                            "is_show": 0,
                                            "sid": "4000663",
                                            "pid": "4000662",
                                            "list": []
                                        },
                                        {
                                            "name": "卫星",
                                            "is_show": 0,
                                            "sid": "4000664",
                                            "pid": "4000662",
                                            "list": []
                                        },
                                        {
                                            "name": "航天器运载工具",
                                            "is_show": 0,
                                            "sid": "4000665",
                                            "pid": "4000662",
                                            "list": []
                                        },
                                        {
                                            "name": "航天地面动力设备",
                                            "is_show": 0,
                                            "sid": "4000666",
                                            "pid": "4000662",
                                            "list": []
                                        },
                                        {
                                            "name": "航天地面控制及测量设备",
                                            "is_show": 0,
                                            "sid": "4000667",
                                            "pid": "4000662",
                                            "list": []
                                        },
                                        {
                                            "name": "其他运载工具",
                                            "is_show": 0,
                                            "sid": "4000668",
                                            "pid": "4000662",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "核设备",
                                    "is_show": 0,
                                    "sid": "4000669",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "核反应堆及启动设备",
                                            "is_show": 0,
                                            "sid": "4000670",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "核反应堆检测装置",
                                            "is_show": 0,
                                            "sid": "4000671",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "废物处理/排出设备",
                                            "is_show": 0,
                                            "sid": "4000672",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "核测量和控制仪器",
                                            "is_show": 0,
                                            "sid": "4000673",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "核测量",
                                            "is_show": 0,
                                            "sid": "4000674",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "核安全设备",
                                            "is_show": 0,
                                            "sid": "4000675",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "核安全机械设备",
                                            "is_show": 0,
                                            "sid": "4000676",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "核辐射防护",
                                            "is_show": 0,
                                            "sid": "4000677",
                                            "pid": "4000669",
                                            "list": []
                                        },
                                        {
                                            "name": "核安全电气设备",
                                            "is_show": 0,
                                            "sid": "4000678",
                                            "pid": "4000669",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "电机",
                                    "is_show": 0,
                                    "sid": "4000679",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "发电设备",
                                            "is_show": 0,
                                            "sid": "4000680",
                                            "pid": "4000679",
                                            "list": []
                                        },
                                        {
                                            "name": "电动机",
                                            "is_show": 0,
                                            "sid": "4000681",
                                            "pid": "4000679",
                                            "list": []
                                        },
                                        {
                                            "name": "微电机",
                                            "is_show": 0,
                                            "sid": "4000682",
                                            "pid": "4000679",
                                            "list": []
                                        },
                                        {
                                            "name": "超导电机",
                                            "is_show": 0,
                                            "sid": "4000683",
                                            "pid": "4000679",
                                            "list": []
                                        },
                                        {
                                            "name": "微电机与超导电机",
                                            "is_show": 0,
                                            "sid": "4000684",
                                            "pid": "4000679",
                                            "list": []
                                        },
                                        {
                                            "name": "分马力电机",
                                            "is_show": 0,
                                            "sid": "4000685",
                                            "pid": "4000679",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "输变电设备/设施",
                                    "is_show": 1,
                                    "sid": "4000686",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "变压器",
                                            "is_show": 1,
                                            "sid": "4000687",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "高压开关",
                                            "is_show": 1,
                                            "sid": "4000688",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "低压电器",
                                            "is_show": 1,
                                            "sid": "4000689",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "换流装置",
                                            "is_show": 1,
                                            "sid": "4000690",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电线/电缆与光缆",
                                            "is_show": 1,
                                            "sid": "4000691",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电线",
                                            "is_show": 1,
                                            "sid": "4000692",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "光缆",
                                            "is_show": 1,
                                            "sid": "4000693",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电缆",
                                            "is_show": 1,
                                            "sid": "4000694",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电池",
                                            "is_show": 1,
                                            "sid": "4000695",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电源",
                                            "is_show": 1,
                                            "sid": "4000696",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电力电容器",
                                            "is_show": 1,
                                            "sid": "4000697",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电池/电源",
                                            "is_show": 1,
                                            "sid": "4000698",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "绝缘产品",
                                            "is_show": 1,
                                            "sid": "4000699",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电动工具",
                                            "is_show": 1,
                                            "sid": "4000700",
                                            "pid": "4000686",
                                            "list": []
                                        },
                                        {
                                            "name": "电动机拖动装置",
                                            "is_show": 1,
                                            "sid": "4000701",
                                            "pid": "4000686",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "电力物资",
                                    "is_show": 0,
                                    "sid": "4000702",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "一次设备",
                                            "is_show": 0,
                                            "sid": "4000703",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "一次设备",
                                            "is_show": 0,
                                            "sid": "4000704",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "二次设备",
                                            "is_show": 0,
                                            "sid": "4000705",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "智能变电站",
                                            "is_show": 0,
                                            "sid": "4000706",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "低压电器",
                                            "is_show": 0,
                                            "sid": "4000707",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "水电设备",
                                            "is_show": 0,
                                            "sid": "4000708",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "电器工具",
                                            "is_show": 0,
                                            "sid": "4000709",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "电动工具",
                                            "is_show": 0,
                                            "sid": "4000710",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "水电配件",
                                            "is_show": 0,
                                            "sid": "4000711",
                                            "pid": "4000702",
                                            "list": []
                                        },
                                        {
                                            "name": "电气仪器仪表",
                                            "is_show": 0,
                                            "sid": "4000712",
                                            "pid": "4000702",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "计算机及网络设备",
                                    "is_show": 0,
                                    "sid": "4000713",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "大中型计算机",
                                            "is_show": 0,
                                            "sid": "4000714",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "大型计算机",
                                            "is_show": 0,
                                            "sid": "4000715",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "中型计算机",
                                            "is_show": 0,
                                            "sid": "4000716",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "小型/微型计算机及工作站",
                                            "is_show": 0,
                                            "sid": "4000717",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "小型计算机",
                                            "is_show": 0,
                                            "sid": "4000718",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "微型计算机",
                                            "is_show": 0,
                                            "sid": "4000719",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "计算机配件",
                                            "is_show": 0,
                                            "sid": "4000720",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "工业过程控制设备",
                                            "is_show": 0,
                                            "sid": "4000721",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "计算机网络安全设备",
                                            "is_show": 0,
                                            "sid": "4000722",
                                            "pid": "4000713",
                                            "list": []
                                        },
                                        {
                                            "name": "计算机配件及外设",
                                            "is_show": 0,
                                            "sid": "4000723",
                                            "pid": "4000713",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "计算机系统软件",
                                    "is_show": 0,
                                    "sid": "4000724",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "系统软件",
                                            "is_show": 0,
                                            "sid": "4000725",
                                            "pid": "4000724",
                                            "list": []
                                        },
                                        {
                                            "name": "支撑软件",
                                            "is_show": 0,
                                            "sid": "4000726",
                                            "pid": "4000724",
                                            "list": []
                                        },
                                        {
                                            "name": "应用软件",
                                            "is_show": 0,
                                            "sid": "4000727",
                                            "pid": "4000724",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "环保设备",
                                    "is_show": 0,
                                    "sid": "4000728",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "环境污染监测仪器设备",
                                            "is_show": 0,
                                            "sid": "4000729",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "水污染治理设备",
                                            "is_show": 0,
                                            "sid": "4000730",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "噪声与振动监测设备",
                                            "is_show": 0,
                                            "sid": "4000731",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "噪声监测设备",
                                            "is_show": 0,
                                            "sid": "4000732",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "振动监测设备",
                                            "is_show": 0,
                                            "sid": "4000733",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "固体废弃物处理设备",
                                            "is_show": 0,
                                            "sid": "4000734",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "固体废弃物 处置 设备",
                                            "is_show": 0,
                                            "sid": "4000735",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "危险废弃物处理 设备",
                                            "is_show": 0,
                                            "sid": "4000736",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "脱硫脱硝设备",
                                            "is_show": 0,
                                            "sid": "4000737",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "燃煤脱硫脱硝设备",
                                            "is_show": 0,
                                            "sid": "4000738",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "固体废弃物处理设备",
                                            "is_show": 0,
                                            "sid": "4000739",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "固体废弃物处理处置设备",
                                            "is_show": 0,
                                            "sid": "4000740",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "危险废弃物处理处置设备",
                                            "is_show": 0,
                                            "sid": "4000741",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "除尘设备",
                                            "is_show": 0,
                                            "sid": "4000742",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "燃煤燃气脱硫/脱硝设备",
                                            "is_show": 0,
                                            "sid": "4000743",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "空气污染治理设备",
                                            "is_show": 0,
                                            "sid": "4000744",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "电磁波污染防治设备",
                                            "is_show": 0,
                                            "sid": "4000745",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "城市固体废弃物处理设备",
                                            "is_show": 0,
                                            "sid": "4000746",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "核与辐射安全监测监控设备",
                                            "is_show": 0,
                                            "sid": "4000747",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "水处理设备",
                                            "is_show": 0,
                                            "sid": "4000748",
                                            "pid": "4000728",
                                            "list": []
                                        },
                                        {
                                            "name": "污泥处理设备",
                                            "is_show": 0,
                                            "sid": "4000749",
                                            "pid": "4000728",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "气象设备",
                                    "is_show": 0,
                                    "sid": "4000750",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "地面气象探测设备",
                                            "is_show": 0,
                                            "sid": "4000751",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "地面气象探测 设备",
                                            "is_show": 0,
                                            "sid": "4000752",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "高空探测系统",
                                            "is_show": 0,
                                            "sid": "4000753",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "高空探测 设备",
                                            "is_show": 0,
                                            "sid": "4000754",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "卫星遥感设备",
                                            "is_show": 0,
                                            "sid": "4000755",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "气象雷达系统",
                                            "is_show": 0,
                                            "sid": "4000756",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "气象计量检定系统",
                                            "is_show": 0,
                                            "sid": "4000757",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "雷电防护设备",
                                            "is_show": 0,
                                            "sid": "4000758",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "天气观测",
                                            "is_show": 0,
                                            "sid": "4000759",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "地基遥感",
                                            "is_show": 0,
                                            "sid": "4000760",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "高空探测设备及软件",
                                            "is_show": 0,
                                            "sid": "4000761",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "大气成分观测分析设备",
                                            "is_show": 0,
                                            "sid": "4000762",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "卫星遥感设备及软件",
                                            "is_show": 0,
                                            "sid": "4000763",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "气象雷达设备及软件",
                                            "is_show": 0,
                                            "sid": "4000764",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "人工影响天气作业设备",
                                            "is_show": 0,
                                            "sid": "4000765",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "气象计量检定设备",
                                            "is_show": 0,
                                            "sid": "4000766",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "农业气象仪器设备",
                                            "is_show": 0,
                                            "sid": "4000767",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "雷电探测及防护设备",
                                            "is_show": 0,
                                            "sid": "4000768",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "空间天气观测设备及软件",
                                            "is_show": 0,
                                            "sid": "4000769",
                                            "pid": "4000750",
                                            "list": []
                                        },
                                        {
                                            "name": "地基遥感设备及软件",
                                            "is_show": 0,
                                            "sid": "4000770",
                                            "pid": "4000750",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "交通信号专用设备",
                                    "is_show": 0,
                                    "sid": "4000771",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "铁路信号设备",
                                            "is_show": 0,
                                            "sid": "4000772",
                                            "pid": "4000771",
                                            "list": []
                                        },
                                        {
                                            "name": "城市轨道信号设备",
                                            "is_show": 0,
                                            "sid": "4000773",
                                            "pid": "4000771",
                                            "list": []
                                        },
                                        {
                                            "name": "轨道信号",
                                            "is_show": 0,
                                            "sid": "4000774",
                                            "pid": "4000771",
                                            "list": []
                                        },
                                        {
                                            "name": "公路信号",
                                            "is_show": 0,
                                            "sid": "4000775",
                                            "pid": "4000771",
                                            "list": []
                                        },
                                        {
                                            "name": "航道信号",
                                            "is_show": 0,
                                            "sid": "4000776",
                                            "pid": "4000771",
                                            "list": []
                                        },
                                        {
                                            "name": "公路信号设备",
                                            "is_show": 0,
                                            "sid": "4000777",
                                            "pid": "4000771",
                                            "list": []
                                        },
                                        {
                                            "name": "水路信号设备",
                                            "is_show": 0,
                                            "sid": "4000778",
                                            "pid": "4000771",
                                            "list": []
                                        },
                                        {
                                            "name": "航道信号设备",
                                            "is_show": 0,
                                            "sid": "4000779",
                                            "pid": "4000771",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "地震监测设备",
                                    "is_show": 0,
                                    "sid": "4000780",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "微震观测设备/仪器",
                                            "is_show": 0,
                                            "sid": "4000781",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "前兆观测设备/仪器",
                                            "is_show": 0,
                                            "sid": "4000782",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "强震动观测设备/仪器",
                                            "is_show": 0,
                                            "sid": "4000783",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "地震观测设备",
                                            "is_show": 0,
                                            "sid": "4000784",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "地震监测设备",
                                            "is_show": 0,
                                            "sid": "4000785",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "地震设备",
                                            "is_show": 0,
                                            "sid": "4000786",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "地震仪器",
                                            "is_show": 0,
                                            "sid": "4000787",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "工程地震",
                                            "is_show": 0,
                                            "sid": "4000788",
                                            "pid": "4000780",
                                            "list": []
                                        },
                                        {
                                            "name": "工程地震设备/仪器",
                                            "is_show": 0,
                                            "sid": "4000789",
                                            "pid": "4000780",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "节能设备",
                                    "is_show": 0,
                                    "sid": "4000790",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "节电器",
                                            "is_show": 0,
                                            "sid": "4000791",
                                            "pid": "4000790",
                                            "list": []
                                        },
                                        {
                                            "name": "变频器",
                                            "is_show": 0,
                                            "sid": "4000792",
                                            "pid": "4000790",
                                            "list": []
                                        },
                                        {
                                            "name": "高效节能设备（锅炉/风机/水泵/电机等）",
                                            "is_show": 0,
                                            "sid": "4000793",
                                            "pid": "4000790",
                                            "list": []
                                        },
                                        {
                                            "name": "高效节能设备",
                                            "is_show": 0,
                                            "sid": "4000794",
                                            "pid": "4000790",
                                            "list": []
                                        },
                                        {
                                            "name": "余热余压利用装备",
                                            "is_show": 0,
                                            "sid": "4000795",
                                            "pid": "4000790",
                                            "list": []
                                        },
                                        {
                                            "name": "余热余压利用",
                                            "is_show": 0,
                                            "sid": "4000796",
                                            "pid": "4000790",
                                            "list": []
                                        },
                                        {
                                            "name": "节油器",
                                            "is_show": 0,
                                            "sid": "4000797",
                                            "pid": "4000790",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "科学/教育设备",
                                    "is_show": 0,
                                    "sid": "4000798",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "通用测试仪",
                                            "is_show": 0,
                                            "sid": "4000799",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "通用分析仪",
                                            "is_show": 0,
                                            "sid": "4000800",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "生化分析仪",
                                            "is_show": 0,
                                            "sid": "4000801",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "光谱分析仪",
                                            "is_show": 0,
                                            "sid": "4000802",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "质谱分析仪",
                                            "is_show": 0,
                                            "sid": "4000803",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "色谱分析仪",
                                            "is_show": 0,
                                            "sid": "4000804",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "公路桥梁试验检测设备",
                                            "is_show": 0,
                                            "sid": "4000805",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "岩土力学地质测试分析设备",
                                            "is_show": 0,
                                            "sid": "4000806",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "土木工程试验仪器/设备",
                                            "is_show": 0,
                                            "sid": "4000807",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "电化教学仪器/设备",
                                            "is_show": 0,
                                            "sid": "4000808",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "电化教学仪器",
                                            "is_show": 0,
                                            "sid": "4000809",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "电化教学设备",
                                            "is_show": 0,
                                            "sid": "4000810",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "音体美仪器",
                                            "is_show": 0,
                                            "sid": "4000811",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "音体美设备",
                                            "is_show": 0,
                                            "sid": "4000812",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "电工教学",
                                            "is_show": 0,
                                            "sid": "4000813",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "电子电工教学仪器/设备",
                                            "is_show": 0,
                                            "sid": "4000814",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "音体美仪器/设备",
                                            "is_show": 0,
                                            "sid": "4000815",
                                            "pid": "4000798",
                                            "list": []
                                        },
                                        {
                                            "name": "电子电工教学仪器/设备",
                                            "is_show": 0,
                                            "sid": "4000816",
                                            "pid": "4000798",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "安全技术防范设备",
                                    "is_show": 0,
                                    "sid": "4000817",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "安防视频监控设备",
                                            "is_show": 0,
                                            "sid": "4000818",
                                            "pid": "4000817",
                                            "list": []
                                        },
                                        {
                                            "name": "入侵探测与防盗报警设备",
                                            "is_show": 0,
                                            "sid": "4000819",
                                            "pid": "4000817",
                                            "list": []
                                        },
                                        {
                                            "name": "安防出入口目标识别与控制设备",
                                            "is_show": 0,
                                            "sid": "4000820",
                                            "pid": "4000817",
                                            "list": []
                                        },
                                        {
                                            "name": "安防实体防护设备",
                                            "is_show": 0,
                                            "sid": "4000821",
                                            "pid": "4000817",
                                            "list": []
                                        },
                                        {
                                            "name": "入侵探测",
                                            "is_show": 0,
                                            "sid": "4000822",
                                            "pid": "4000817",
                                            "list": []
                                        },
                                        {
                                            "name": "防盗报警设备",
                                            "is_show": 0,
                                            "sid": "4000823",
                                            "pid": "4000817",
                                            "list": []
                                        },
                                        {
                                            "name": "防爆安全检查设备",
                                            "is_show": 0,
                                            "sid": "4000824",
                                            "pid": "4000817",
                                            "list": []
                                        },
                                        {
                                            "name": "移动目标反劫防盗设备",
                                            "is_show": 0,
                                            "sid": "4000825",
                                            "pid": "4000817",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "其他专用机械",
                                    "is_show": 0,
                                    "sid": "4000826",
                                    "pid": "4000338",
                                    "list": [
                                        {
                                            "name": "商业机械",
                                            "is_show": 0,
                                            "sid": "4000827",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "邮政机械",
                                            "is_show": 0,
                                            "sid": "4000828",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "水工机械",
                                            "is_show": 0,
                                            "sid": "4000829",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "水力机械（不含水轮机）",
                                            "is_show": 0,
                                            "sid": "4000830",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "蒸汽/燃气/水轮机",
                                            "is_show": 0,
                                            "sid": "4000831",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "风力机械",
                                            "is_show": 0,
                                            "sid": "4000832",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "地震测试专用器械",
                                            "is_show": 0,
                                            "sid": "4000833",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "测绘专用设备",
                                            "is_show": 0,
                                            "sid": "4000834",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "测绘专用仪器",
                                            "is_show": 0,
                                            "sid": "4000835",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "测绘专用器械",
                                            "is_show": 0,
                                            "sid": "4000836",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "计量设备",
                                            "is_show": 0,
                                            "sid": "4000837",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "警用装备",
                                            "is_show": 0,
                                            "sid": "4000838",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "警用器械",
                                            "is_show": 0,
                                            "sid": "4000839",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "警用装备及器械",
                                            "is_show": 0,
                                            "sid": "4000840",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "体育器械",
                                            "is_show": 0,
                                            "sid": "4000841",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "印刷机械",
                                            "is_show": 0,
                                            "sid": "4000842",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "人体生物识别设备",
                                            "is_show": 0,
                                            "sid": "4000843",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "道路交通安全设备",
                                            "is_show": 0,
                                            "sid": "4000844",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "水文监测专用设备",
                                            "is_show": 0,
                                            "sid": "4000845",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "水文监测设备",
                                            "is_show": 0,
                                            "sid": "4000846",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "风机与压缩机",
                                            "is_show": 0,
                                            "sid": "4000847",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "风机",
                                            "is_show": 0,
                                            "sid": "4000848",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "压缩机",
                                            "is_show": 0,
                                            "sid": "4000849",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "制冷与采暖空调设备",
                                            "is_show": 0,
                                            "sid": "4000850",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "制冷空调设备",
                                            "is_show": 0,
                                            "sid": "4000851",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "采暖空调设备",
                                            "is_show": 0,
                                            "sid": "4000852",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "减速机",
                                            "is_show": 0,
                                            "sid": "4000853",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "气体分离设备",
                                            "is_show": 0,
                                            "sid": "4000854",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "泵与阀门",
                                            "is_show": 0,
                                            "sid": "4000855",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "消防设备",
                                            "is_show": 0,
                                            "sid": "4000856",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "流体传动与控制",
                                            "is_show": 0,
                                            "sid": "4000857",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "减速机及基础零部件",
                                            "is_show": 0,
                                            "sid": "4000858",
                                            "pid": "4000826",
                                            "list": []
                                        },
                                        {
                                            "name": "发动机",
                                            "is_show": 0,
                                            "sid": "4000859",
                                            "pid": "4000826",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "医疗器械",
                            "is_show": 1,
                            "sid": "4000860",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "医疗器械",
                                    "is_show": 1,
                                    "sid": "4000861",
                                    "pid": "4000860",
                                    "list": [
                                        {
                                            "name": "手术器械",
                                            "is_show": 1,
                                            "sid": "4000862",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "注射穿刺器械",
                                            "is_show": 1,
                                            "sid": "4000863",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "普通诊察器械",
                                            "is_show": 1,
                                            "sid": "4000864",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用电子仪器设备",
                                            "is_show": 1,
                                            "sid": "4000865",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用光学器具/仪器及内窥镜设备",
                                            "is_show": 0,
                                            "sid": "4000866",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用超声仪器及有关设备",
                                            "is_show": 1,
                                            "sid": "4000867",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用激光仪器设备",
                                            "is_show": 1,
                                            "sid": "4000868",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用高频仪器设备",
                                            "is_show": 1,
                                            "sid": "4000869",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "物理治疗及康复设备",
                                            "is_show": 1,
                                            "sid": "4000870",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "中医器械",
                                            "is_show": 0,
                                            "sid": "4000871",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用磁共振设备",
                                            "is_show": 0,
                                            "sid": "4000872",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用X射线设备及附属设备/备件",
                                            "is_show": 0,
                                            "sid": "4000873",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用高能射线设备",
                                            "is_show": 0,
                                            "sid": "4000874",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用核素设备",
                                            "is_show": 0,
                                            "sid": "4000875",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用射线防护用品/装置",
                                            "is_show": 0,
                                            "sid": "4000876",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "临床检验分析仪器",
                                            "is_show": 0,
                                            "sid": "4000877",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用化验和基础设备器具",
                                            "is_show": 0,
                                            "sid": "4000878",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "体外循环及血液处理设备",
                                            "is_show": 0,
                                            "sid": "4000879",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "植入材料和人工器官",
                                            "is_show": 0,
                                            "sid": "4000880",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "手术室/急救室/诊疗室设备及器具",
                                            "is_show": 0,
                                            "sid": "4000881",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "口腔科设备及器具",
                                            "is_show": 0,
                                            "sid": "4000882",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "病房护理设备及器具",
                                            "is_show": 0,
                                            "sid": "4000883",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "消毒和灭菌设备及器具",
                                            "is_show": 0,
                                            "sid": "4000884",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用冷疗/低温/冷藏设备及器具",
                                            "is_show": 0,
                                            "sid": "4000885",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "口腔科材料",
                                            "is_show": 0,
                                            "sid": "4000886",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用卫生材料及敷料",
                                            "is_show": 0,
                                            "sid": "4000887",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用缝合材料及粘合剂",
                                            "is_show": 0,
                                            "sid": "4000888",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医用高分子材料及制品",
                                            "is_show": 0,
                                            "sid": "4000889",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "介入器材",
                                            "is_show": 0,
                                            "sid": "4000890",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医院网络设备及软件",
                                            "is_show": 0,
                                            "sid": "4000891",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医疗专用车设备",
                                            "is_show": 0,
                                            "sid": "4000892",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医疗垃圾处理系统",
                                            "is_show": 0,
                                            "sid": "4000893",
                                            "pid": "4000861",
                                            "list": []
                                        },
                                        {
                                            "name": "医药包装自动化",
                                            "is_show": 0,
                                            "sid": "4000894",
                                            "pid": "4000861",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "金属材料",
                            "is_show": 0,
                            "sid": "4000895",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "黑色金属",
                                    "is_show": 0,
                                    "sid": "4000896",
                                    "pid": "4000895",
                                    "list": [
                                        {
                                            "name": "生铁/钢锭",
                                            "is_show": 0,
                                            "sid": "4000897",
                                            "pid": "4000896",
                                            "list": []
                                        },
                                        {
                                            "name": "黑色金属产品",
                                            "is_show": 0,
                                            "sid": "4000898",
                                            "pid": "4000896",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "有色金属",
                                    "is_show": 0,
                                    "sid": "4000899",
                                    "pid": "4000895",
                                    "list": [
                                        {
                                            "name": "稀有稀土金属",
                                            "is_show": 0,
                                            "sid": "4000900",
                                            "pid": "4000899",
                                            "list": []
                                        },
                                        {
                                            "name": "粉末冶金",
                                            "is_show": 0,
                                            "sid": "4000901",
                                            "pid": "4000899",
                                            "list": []
                                        },
                                        {
                                            "name": "有色金属制品",
                                            "is_show": 0,
                                            "sid": "4000902",
                                            "pid": "4000899",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "合金",
                                    "is_show": 0,
                                    "sid": "4000903",
                                    "pid": "4000895",
                                    "list": [
                                        {
                                            "name": "铁合金",
                                            "is_show": 0,
                                            "sid": "4000904",
                                            "pid": "4000903",
                                            "list": []
                                        },
                                        {
                                            "name": "有色金属合金",
                                            "is_show": 0,
                                            "sid": "4000905",
                                            "pid": "4000903",
                                            "list": []
                                        },
                                        {
                                            "name": "合金产品",
                                            "is_show": 0,
                                            "sid": "4000906",
                                            "pid": "4000903",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "石油及其制品",
                            "is_show": 0,
                            "sid": "4000907",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "原油",
                                    "is_show": 0,
                                    "sid": "4000908",
                                    "pid": "4000907",
                                    "list": [
                                        {
                                            "name": "原油采购",
                                            "is_show": 0,
                                            "sid": "4000909",
                                            "pid": "4000908",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "天然气",
                                    "is_show": 0,
                                    "sid": "4000910",
                                    "pid": "4000907",
                                    "list": [
                                        {
                                            "name": "天然气采购",
                                            "is_show": 0,
                                            "sid": "4000911",
                                            "pid": "4000910",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "石油制品",
                                    "is_show": 0,
                                    "sid": "4000912",
                                    "pid": "4000907",
                                    "list": [
                                        {
                                            "name": "汽油/煤油/柴油和润滑油",
                                            "is_show": 0,
                                            "sid": "4000913",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "汽油采购",
                                            "is_show": 0,
                                            "sid": "4000914",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "煤油采购",
                                            "is_show": 0,
                                            "sid": "4000915",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "柴油采购",
                                            "is_show": 0,
                                            "sid": "4000916",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "润滑油采购",
                                            "is_show": 0,
                                            "sid": "4000917",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "沥青焦采购",
                                            "is_show": 0,
                                            "sid": "4000918",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "石油焦采购",
                                            "is_show": 0,
                                            "sid": "4000919",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "阳极采购",
                                            "is_show": 0,
                                            "sid": "4000920",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "阴极采购",
                                            "is_show": 0,
                                            "sid": "4000921",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "电极糊采购",
                                            "is_show": 0,
                                            "sid": "4000922",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "石蜡采购",
                                            "is_show": 0,
                                            "sid": "4000923",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "沥青焦/石油焦",
                                            "is_show": 0,
                                            "sid": "4000924",
                                            "pid": "4000912",
                                            "list": []
                                        },
                                        {
                                            "name": "阳极/阴极/电极糊碳块",
                                            "is_show": 0,
                                            "sid": "4000925",
                                            "pid": "4000912",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "煤炭煤层气及其制品",
                            "is_show": 0,
                            "sid": "4000926",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "煤炭",
                                    "is_show": 0,
                                    "sid": "4000927",
                                    "pid": "4000926",
                                    "list": [
                                        {
                                            "name": "原煤/煤矸石",
                                            "is_show": 0,
                                            "sid": "4000928",
                                            "pid": "4000927",
                                            "list": []
                                        },
                                        {
                                            "name": "原煤采购",
                                            "is_show": 0,
                                            "sid": "4000929",
                                            "pid": "4000927",
                                            "list": []
                                        },
                                        {
                                            "name": "煤矸石采购",
                                            "is_show": 0,
                                            "sid": "4000930",
                                            "pid": "4000927",
                                            "list": []
                                        },
                                        {
                                            "name": "洗精煤采购",
                                            "is_show": 0,
                                            "sid": "4000931",
                                            "pid": "4000927",
                                            "list": []
                                        },
                                        {
                                            "name": "可燃性片岩采购",
                                            "is_show": 0,
                                            "sid": "4000932",
                                            "pid": "4000927",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "煤炭制品",
                                    "is_show": 0,
                                    "sid": "4000933",
                                    "pid": "4000926",
                                    "list": [
                                        {
                                            "name": "焦炭采购",
                                            "is_show": 0,
                                            "sid": "4000934",
                                            "pid": "4000933",
                                            "list": []
                                        },
                                        {
                                            "name": "型煤采购",
                                            "is_show": 0,
                                            "sid": "4000935",
                                            "pid": "4000933",
                                            "list": []
                                        },
                                        {
                                            "name": "水煤浆采购",
                                            "is_show": 0,
                                            "sid": "4000936",
                                            "pid": "4000933",
                                            "list": []
                                        },
                                        {
                                            "name": "煤液化产品采购",
                                            "is_show": 0,
                                            "sid": "4000937",
                                            "pid": "4000933",
                                            "list": []
                                        },
                                        {
                                            "name": "煤气化产品采购",
                                            "is_show": 0,
                                            "sid": "4000938",
                                            "pid": "4000933",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "煤层气",
                                    "is_show": 0,
                                    "sid": "4000939",
                                    "pid": "4000926",
                                    "list": [
                                        {
                                            "name": "煤层气",
                                            "is_show": 0,
                                            "sid": "4000940",
                                            "pid": "4000939",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "化工材料及其制品",
                            "is_show": 1,
                            "sid": "4000941",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "无机化学原料",
                                    "is_show": 0,
                                    "sid": "4000942",
                                    "pid": "4000941",
                                    "list": [
                                        {
                                            "name": "无机化学原料",
                                            "is_show": 0,
                                            "sid": "4000943",
                                            "pid": "4000942",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "有机化工材料",
                                    "is_show": 0,
                                    "sid": "4000944",
                                    "pid": "4000941",
                                    "list": [
                                        {
                                            "name": "有机化工材料",
                                            "is_show": 0,
                                            "sid": "4000945",
                                            "pid": "4000944",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "合成材料及专用化工品",
                                    "is_show": 1,
                                    "sid": "4000946",
                                    "pid": "4000941",
                                    "list": [
                                        {
                                            "name": "涂料采购",
                                            "is_show": 1,
                                            "sid": "4000947",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "化肥/农药",
                                            "is_show": 1,
                                            "sid": "4000948",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "橡胶/塑料及其制品",
                                            "is_show": 1,
                                            "sid": "4000949",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "玻璃及其制品",
                                            "is_show": 1,
                                            "sid": "4000950",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "颜料/染料",
                                            "is_show": 1,
                                            "sid": "4000951",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "化肥采购",
                                            "is_show": 1,
                                            "sid": "4000952",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "农药采购",
                                            "is_show": 1,
                                            "sid": "4000953",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "橡胶采购",
                                            "is_show": 1,
                                            "sid": "4000954",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "塑料采购",
                                            "is_show": 1,
                                            "sid": "4000955",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "玻璃采购",
                                            "is_show": 1,
                                            "sid": "4000956",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "颜料采购",
                                            "is_show": 1,
                                            "sid": "4000957",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "染料采购",
                                            "is_show": 1,
                                            "sid": "4000958",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "专用化学品",
                                            "is_show": 1,
                                            "sid": "4000959",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "精细化学品",
                                            "is_show": 1,
                                            "sid": "4000960",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "合成材料采购",
                                            "is_show": 1,
                                            "sid": "4000961",
                                            "pid": "4000946",
                                            "list": []
                                        },
                                        {
                                            "name": "专用化学品和精细化学品",
                                            "is_show": 1,
                                            "sid": "4000962",
                                            "pid": "4000946",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "建筑材料",
                            "is_show": 0,
                            "sid": "4000963",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "水泥及水泥制品",
                                    "is_show": 0,
                                    "sid": "4000964",
                                    "pid": "4000963",
                                    "list": [
                                        {
                                            "name": "水泥与水泥熟料",
                                            "is_show": 0,
                                            "sid": "4000965",
                                            "pid": "4000964",
                                            "list": []
                                        },
                                        {
                                            "name": "水泥采购",
                                            "is_show": 0,
                                            "sid": "4000966",
                                            "pid": "4000964",
                                            "list": []
                                        },
                                        {
                                            "name": "水泥熟料采购",
                                            "is_show": 0,
                                            "sid": "4000967",
                                            "pid": "4000964",
                                            "list": []
                                        },
                                        {
                                            "name": "水泥制品采购",
                                            "is_show": 0,
                                            "sid": "4000968",
                                            "pid": "4000964",
                                            "list": []
                                        },
                                        {
                                            "name": "水泥制品",
                                            "is_show": 0,
                                            "sid": "4000969",
                                            "pid": "4000964",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "木材",
                                    "is_show": 0,
                                    "sid": "4000970",
                                    "pid": "4000963",
                                    "list": [
                                        {
                                            "name": "原木/板方材",
                                            "is_show": 0,
                                            "sid": "4000971",
                                            "pid": "4000970",
                                            "list": []
                                        },
                                        {
                                            "name": "复合板材",
                                            "is_show": 0,
                                            "sid": "4000972",
                                            "pid": "4000970",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "石材",
                                    "is_show": 0,
                                    "sid": "4000973",
                                    "pid": "4000963",
                                    "list": [
                                        {
                                            "name": "人造石材",
                                            "is_show": 0,
                                            "sid": "4000974",
                                            "pid": "4000973",
                                            "list": []
                                        },
                                        {
                                            "name": "天然石材",
                                            "is_show": 0,
                                            "sid": "4000975",
                                            "pid": "4000973",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "陶瓷制品",
                                    "is_show": 0,
                                    "sid": "4000976",
                                    "pid": "4000963",
                                    "list": [
                                        {
                                            "name": "建筑陶瓷及制品",
                                            "is_show": 0,
                                            "sid": "4000977",
                                            "pid": "4000976",
                                            "list": []
                                        },
                                        {
                                            "name": "卫生陶瓷及制品",
                                            "is_show": 0,
                                            "sid": "4000978",
                                            "pid": "4000976",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "钢材",
                                    "is_show": 0,
                                    "sid": "4000979",
                                    "pid": "4000963",
                                    "list": [
                                        {
                                            "name": "钢材",
                                            "is_show": 0,
                                            "sid": "4000980",
                                            "pid": "4000979",
                                            "list": []
                                        },
                                        {
                                            "name": "钢管",
                                            "is_show": 0,
                                            "sid": "4000981",
                                            "pid": "4000979",
                                            "list": []
                                        },
                                        {
                                            "name": "角钢",
                                            "is_show": 0,
                                            "sid": "4000982",
                                            "pid": "4000979",
                                            "list": []
                                        },
                                        {
                                            "name": "槽钢",
                                            "is_show": 0,
                                            "sid": "4000983",
                                            "pid": "4000979",
                                            "list": []
                                        },
                                        {
                                            "name": "螺纹钢",
                                            "is_show": 0,
                                            "sid": "4000984",
                                            "pid": "4000979",
                                            "list": []
                                        },
                                        {
                                            "name": "型钢",
                                            "is_show": 0,
                                            "sid": "4000985",
                                            "pid": "4000979",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "其他建筑材料",
                                    "is_show": 0,
                                    "sid": "4000986",
                                    "pid": "4000963",
                                    "list": [
                                        {
                                            "name": "隔热保温材料",
                                            "is_show": 0,
                                            "sid": "4000987",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "防水材料/密封材料",
                                            "is_show": 0,
                                            "sid": "4000988",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "防水材料",
                                            "is_show": 0,
                                            "sid": "4000989",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "密封材料",
                                            "is_show": 0,
                                            "sid": "4000990",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "混凝土",
                                            "is_show": 0,
                                            "sid": "4000991",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "油漆",
                                            "is_show": 0,
                                            "sid": "4000992",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "涂料",
                                            "is_show": 0,
                                            "sid": "4000993",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "砂石",
                                            "is_show": 0,
                                            "sid": "4000994",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "电工绝缘材料",
                                            "is_show": 0,
                                            "sid": "4000995",
                                            "pid": "4000986",
                                            "list": []
                                        },
                                        {
                                            "name": "特种建筑材料",
                                            "is_show": 0,
                                            "sid": "4000996",
                                            "pid": "4000986",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "新型材料",
                                    "is_show": 0,
                                    "sid": "4000997",
                                    "pid": "4000963",
                                    "list": [
                                        {
                                            "name": "纳米技术与纳米材料",
                                            "is_show": 0,
                                            "sid": "4000998",
                                            "pid": "4000997",
                                            "list": []
                                        },
                                        {
                                            "name": "其他新型建筑材料",
                                            "is_show": 0,
                                            "sid": "4000999",
                                            "pid": "4000997",
                                            "list": []
                                        },
                                        {
                                            "name": "利废建筑材料",
                                            "is_show": 0,
                                            "sid": "4001000",
                                            "pid": "4000997",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "药品",
                            "is_show": 0,
                            "sid": "4001001",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "内科",
                                    "is_show": 0,
                                    "sid": "4001002",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "普通内科",
                                            "is_show": 0,
                                            "sid": "4001003",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "心血管内科",
                                            "is_show": 0,
                                            "sid": "4001004",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "呼吸内科",
                                            "is_show": 0,
                                            "sid": "4001005",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "神经内科",
                                            "is_show": 0,
                                            "sid": "4001006",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "消化内科",
                                            "is_show": 0,
                                            "sid": "4001007",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "血液内科",
                                            "is_show": 0,
                                            "sid": "4001008",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "肾内科",
                                            "is_show": 0,
                                            "sid": "4001009",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "内分泌内科",
                                            "is_show": 0,
                                            "sid": "4001010",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "风湿病学",
                                            "is_show": 0,
                                            "sid": "4001011",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "感染性疾病科",
                                            "is_show": 0,
                                            "sid": "4001012",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "急诊医学",
                                            "is_show": 0,
                                            "sid": "4001013",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "康复医学",
                                            "is_show": 0,
                                            "sid": "4001014",
                                            "pid": "4001002",
                                            "list": []
                                        },
                                        {
                                            "name": "老年医学",
                                            "is_show": 0,
                                            "sid": "4001015",
                                            "pid": "4001002",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "外科",
                                    "is_show": 0,
                                    "sid": "4001016",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "普通外科",
                                            "is_show": 0,
                                            "sid": "4001017",
                                            "pid": "4001016",
                                            "list": []
                                        },
                                        {
                                            "name": "神经外科",
                                            "is_show": 0,
                                            "sid": "4001018",
                                            "pid": "4001016",
                                            "list": []
                                        },
                                        {
                                            "name": "胸心外科",
                                            "is_show": 0,
                                            "sid": "4001019",
                                            "pid": "4001016",
                                            "list": []
                                        },
                                        {
                                            "name": "泌尿外科",
                                            "is_show": 0,
                                            "sid": "4001020",
                                            "pid": "4001016",
                                            "list": []
                                        },
                                        {
                                            "name": "骨外科",
                                            "is_show": 0,
                                            "sid": "4001021",
                                            "pid": "4001016",
                                            "list": []
                                        },
                                        {
                                            "name": "烧伤外科",
                                            "is_show": 0,
                                            "sid": "4001022",
                                            "pid": "4001016",
                                            "list": []
                                        },
                                        {
                                            "name": "整形外科",
                                            "is_show": 0,
                                            "sid": "4001023",
                                            "pid": "4001016",
                                            "list": []
                                        },
                                        {
                                            "name": "创伤外科",
                                            "is_show": 0,
                                            "sid": "4001024",
                                            "pid": "4001016",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "妇产科（计划生育）",
                                    "is_show": 0,
                                    "sid": "4001025",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "妇科",
                                            "is_show": 0,
                                            "sid": "4001026",
                                            "pid": "4001025",
                                            "list": []
                                        },
                                        {
                                            "name": "产科",
                                            "is_show": 0,
                                            "sid": "4001027",
                                            "pid": "4001025",
                                            "list": []
                                        },
                                        {
                                            "name": "生殖医学",
                                            "is_show": 0,
                                            "sid": "4001028",
                                            "pid": "4001025",
                                            "list": []
                                        },
                                        {
                                            "name": "计划生育",
                                            "is_show": 0,
                                            "sid": "4001029",
                                            "pid": "4001025",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "儿科",
                                    "is_show": 0,
                                    "sid": "4001030",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "小儿内科",
                                            "is_show": 0,
                                            "sid": "4001031",
                                            "pid": "4001030",
                                            "list": []
                                        },
                                        {
                                            "name": "小儿外科",
                                            "is_show": 0,
                                            "sid": "4001032",
                                            "pid": "4001030",
                                            "list": []
                                        },
                                        {
                                            "name": "新生儿科",
                                            "is_show": 0,
                                            "sid": "4001033",
                                            "pid": "4001030",
                                            "list": []
                                        },
                                        {
                                            "name": "儿童保健科",
                                            "is_show": 0,
                                            "sid": "4001034",
                                            "pid": "4001030",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "口腔科",
                                    "is_show": 0,
                                    "sid": "4001035",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "口腔科",
                                            "is_show": 0,
                                            "sid": "4001036",
                                            "pid": "4001035",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "眼科",
                                    "is_show": 0,
                                    "sid": "4001037",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "眼科",
                                            "is_show": 0,
                                            "sid": "4001038",
                                            "pid": "4001037",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "耳鼻咽喉科",
                                    "is_show": 0,
                                    "sid": "4001039",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "耳鼻咽喉科",
                                            "is_show": 0,
                                            "sid": "4001040",
                                            "pid": "4001039",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "皮肤科",
                                    "is_show": 0,
                                    "sid": "4001041",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "皮肤科",
                                            "is_show": 0,
                                            "sid": "4001042",
                                            "pid": "4001041",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "精神科",
                                    "is_show": 0,
                                    "sid": "4001043",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "精神病学",
                                            "is_show": 0,
                                            "sid": "4001044",
                                            "pid": "4001043",
                                            "list": []
                                        },
                                        {
                                            "name": "医学心理学",
                                            "is_show": 0,
                                            "sid": "4001045",
                                            "pid": "4001043",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "肿瘤科",
                                    "is_show": 0,
                                    "sid": "4001046",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "肿瘤内科（含妇科肿瘤）",
                                            "is_show": 0,
                                            "sid": "4001047",
                                            "pid": "4001046",
                                            "list": []
                                        },
                                        {
                                            "name": "肿瘤外科",
                                            "is_show": 0,
                                            "sid": "4001048",
                                            "pid": "4001046",
                                            "list": []
                                        },
                                        {
                                            "name": "放疗肿瘤学",
                                            "is_show": 0,
                                            "sid": "4001049",
                                            "pid": "4001046",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "中医",
                                    "is_show": 0,
                                    "sid": "4001050",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "中医内科",
                                            "is_show": 0,
                                            "sid": "4001051",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医妇科",
                                            "is_show": 0,
                                            "sid": "4001052",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医儿科",
                                            "is_show": 0,
                                            "sid": "4001053",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医外科",
                                            "is_show": 0,
                                            "sid": "4001054",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医骨伤科",
                                            "is_show": 0,
                                            "sid": "4001055",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医皮肤科",
                                            "is_show": 0,
                                            "sid": "4001056",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医肛肠科",
                                            "is_show": 0,
                                            "sid": "4001057",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "针灸",
                                            "is_show": 0,
                                            "sid": "4001058",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "按摩推拿",
                                            "is_show": 0,
                                            "sid": "4001059",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医五官科",
                                            "is_show": 0,
                                            "sid": "4001060",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医肿瘤科",
                                            "is_show": 0,
                                            "sid": "4001061",
                                            "pid": "4001050",
                                            "list": []
                                        },
                                        {
                                            "name": "中医精神病科",
                                            "is_show": 0,
                                            "sid": "4001062",
                                            "pid": "4001050",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "民族医学",
                                    "is_show": 0,
                                    "sid": "4001063",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "藏医学",
                                            "is_show": 0,
                                            "sid": "4001064",
                                            "pid": "4001063",
                                            "list": []
                                        },
                                        {
                                            "name": "蒙医学",
                                            "is_show": 0,
                                            "sid": "4001065",
                                            "pid": "4001063",
                                            "list": []
                                        },
                                        {
                                            "name": "维医学",
                                            "is_show": 0,
                                            "sid": "4001066",
                                            "pid": "4001063",
                                            "list": []
                                        },
                                        {
                                            "name": "傣医学",
                                            "is_show": 0,
                                            "sid": "4001067",
                                            "pid": "4001063",
                                            "list": []
                                        },
                                        {
                                            "name": "朝医学",
                                            "is_show": 0,
                                            "sid": "4001068",
                                            "pid": "4001063",
                                            "list": []
                                        },
                                        {
                                            "name": "壮医学",
                                            "is_show": 0,
                                            "sid": "4001069",
                                            "pid": "4001063",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "麻醉科",
                                    "is_show": 0,
                                    "sid": "4001070",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "麻醉学",
                                            "is_show": 0,
                                            "sid": "4001071",
                                            "pid": "4001070",
                                            "list": []
                                        },
                                        {
                                            "name": "疼痛治疗学",
                                            "is_show": 0,
                                            "sid": "4001072",
                                            "pid": "4001070",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "中西医结合科",
                                    "is_show": 0,
                                    "sid": "4001073",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "中西医结合科",
                                            "is_show": 0,
                                            "sid": "4001074",
                                            "pid": "4001073",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "病理科",
                                    "is_show": 0,
                                    "sid": "4001075",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "病理科",
                                            "is_show": 0,
                                            "sid": "4001076",
                                            "pid": "4001075",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "医技",
                                    "is_show": 0,
                                    "sid": "4001077",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "临床医学检验",
                                            "is_show": 0,
                                            "sid": "4001078",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "卫生检验",
                                            "is_show": 0,
                                            "sid": "4001079",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "心电图",
                                            "is_show": 0,
                                            "sid": "4001080",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "脑电图",
                                            "is_show": 0,
                                            "sid": "4001081",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "理疗",
                                            "is_show": 0,
                                            "sid": "4001082",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "病案",
                                            "is_show": 0,
                                            "sid": "4001083",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "医用影像类",
                                            "is_show": 0,
                                            "sid": "4001084",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "生物医学工程",
                                            "is_show": 0,
                                            "sid": "4001085",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "激光医学",
                                            "is_show": 0,
                                            "sid": "4001086",
                                            "pid": "4001077",
                                            "list": []
                                        },
                                        {
                                            "name": "高压氧医学",
                                            "is_show": 0,
                                            "sid": "4001087",
                                            "pid": "4001077",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "疾控与公共卫生",
                                    "is_show": 0,
                                    "sid": "4001088",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "环境卫生",
                                            "is_show": 0,
                                            "sid": "4001089",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "营养与食品卫生",
                                            "is_show": 0,
                                            "sid": "4001090",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "学校卫生与少儿卫生",
                                            "is_show": 0,
                                            "sid": "4001091",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "放射卫生",
                                            "is_show": 0,
                                            "sid": "4001092",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "卫生毒理",
                                            "is_show": 0,
                                            "sid": "4001093",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "传染性疾病控制",
                                            "is_show": 0,
                                            "sid": "4001094",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "慢性非传染性疾病控制",
                                            "is_show": 0,
                                            "sid": "4001095",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "地方病控制",
                                            "is_show": 0,
                                            "sid": "4001096",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "寄生虫病控制",
                                            "is_show": 0,
                                            "sid": "4001097",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "儿童保健",
                                            "is_show": 0,
                                            "sid": "4001098",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "妇幼保健",
                                            "is_show": 0,
                                            "sid": "4001099",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "职业卫生",
                                            "is_show": 0,
                                            "sid": "4001100",
                                            "pid": "4001088",
                                            "list": []
                                        },
                                        {
                                            "name": "健康教育与健康促进",
                                            "is_show": 0,
                                            "sid": "4001101",
                                            "pid": "4001088",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "护理",
                                    "is_show": 0,
                                    "sid": "4001102",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "临床护理",
                                            "is_show": 0,
                                            "sid": "4001103",
                                            "pid": "4001102",
                                            "list": []
                                        },
                                        {
                                            "name": "透析护理",
                                            "is_show": 0,
                                            "sid": "4001104",
                                            "pid": "4001102",
                                            "list": []
                                        },
                                        {
                                            "name": "妇产科护理",
                                            "is_show": 0,
                                            "sid": "4001105",
                                            "pid": "4001102",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "药学",
                                    "is_show": 0,
                                    "sid": "4001106",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "中药",
                                            "is_show": 0,
                                            "sid": "4001107",
                                            "pid": "4001106",
                                            "list": []
                                        },
                                        {
                                            "name": "化学药品",
                                            "is_show": 0,
                                            "sid": "4001108",
                                            "pid": "4001106",
                                            "list": []
                                        },
                                        {
                                            "name": "生物制品",
                                            "is_show": 0,
                                            "sid": "4001109",
                                            "pid": "4001106",
                                            "list": []
                                        },
                                        {
                                            "name": "药用包装产品",
                                            "is_show": 0,
                                            "sid": "4001110",
                                            "pid": "4001106",
                                            "list": []
                                        },
                                        {
                                            "name": "临床医学",
                                            "is_show": 0,
                                            "sid": "4001111",
                                            "pid": "4001106",
                                            "list": []
                                        },
                                        {
                                            "name": "伦理学",
                                            "is_show": 0,
                                            "sid": "4001112",
                                            "pid": "4001106",
                                            "list": []
                                        },
                                        {
                                            "name": "药物经济学",
                                            "is_show": 0,
                                            "sid": "4001113",
                                            "pid": "4001106",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "法医学",
                                    "is_show": 0,
                                    "sid": "4001114",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "法医学",
                                            "is_show": 0,
                                            "sid": "4001115",
                                            "pid": "4001114",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "戒毒医学",
                                    "is_show": 0,
                                    "sid": "4001116",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "戒毒医学",
                                            "is_show": 0,
                                            "sid": "4001117",
                                            "pid": "4001116",
                                            "list": []
                                        }
                                    ]
                                },
                                {
                                    "name": "环化药剂",
                                    "is_show": 0,
                                    "sid": "4001118",
                                    "pid": "4001001",
                                    "list": [
                                        {
                                            "name": "化学混凝沉淀类药剂",
                                            "is_show": 0,
                                            "sid": "4001119",
                                            "pid": "4001118",
                                            "list": []
                                        },
                                        {
                                            "name": "氧化-还原类药剂",
                                            "is_show": 0,
                                            "sid": "4001120",
                                            "pid": "4001118",
                                            "list": []
                                        },
                                        {
                                            "name": "消毒类药剂",
                                            "is_show": 0,
                                            "sid": "4001121",
                                            "pid": "4001118",
                                            "list": []
                                        },
                                        {
                                            "name": "除臭类药剂",
                                            "is_show": 0,
                                            "sid": "4001122",
                                            "pid": "4001118",
                                            "list": []
                                        },
                                        {
                                            "name": "生物助剂",
                                            "is_show": 0,
                                            "sid": "4001123",
                                            "pid": "4001118",
                                            "list": []
                                        },
                                        {
                                            "name": "生物酶",
                                            "is_show": 0,
                                            "sid": "4001124",
                                            "pid": "4001118",
                                            "list": []
                                        },
                                        {
                                            "name": "生物助剂（生物酶）",
                                            "is_show": 0,
                                            "sid": "4001125",
                                            "pid": "4001118",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "name": "其他类",
                            "is_show": 0,
                            "sid": "4001126",
                            "pid": "4000002",
                            "list": [
                                {
                                    "name": "其他货物",
                                    "is_show": 0,
                                    "sid": "4001127",
                                    "pid": "4001126",
                                    "list": [
                                        {
                                            "name": "办公设备",
                                            "is_show": 0,
                                            "sid": "4001128",
                                            "pid": "4001127",
                                            "list": []
                                        },
                                        {
                                            "name": "家具",
                                            "is_show": 0,
                                            "sid": "4001129",
                                            "pid": "4001127",
                                            "list": []
                                        },
                                        {
                                            "name": "办公耗材",
                                            "is_show": 0,
                                            "sid": "4001130",
                                            "pid": "4001127",
                                            "list": []
                                        },
                                        {
                                            "name": "厨房设备",
                                            "is_show": 0,
                                            "sid": "4001131",
                                            "pid": "4001127",
                                            "list": []
                                        },
                                        {
                                            "name": "洗衣机",
                                            "is_show": 0,
                                            "sid": "4001132",
                                            "pid": "4001127",
                                            "list": []
                                        },
                                        {
                                            "name": "服装",
                                            "is_show": 0,
                                            "sid": "4001133",
                                            "pid": "4001127",
                                            "list": []
                                        },
                                        {
                                            "name": "图书",
                                            "is_show": 0,
                                            "sid": "4001134",
                                            "pid": "4001127",
                                            "list": []
                                        },
                                        {
                                            "name": "音像/电子出版物",
                                            "is_show": 0,
                                            "sid": "4001135",
                                            "pid": "4001127",
                                            "list": []
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "服务类",
                    "is_show": 1,
                    "sid": "4000003",
                    "pid": "0",
                    "list": [
                        {
                            "name": "工程设计",
                            "is_show": 1,
                            "sid": "4001136",
                            "pid": "4000003",
                            "list": [
                                {
                                    "name": "煤炭",
                                    "is_show": 1,
                                    "sid": "4001137",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "化工石化医药",
                                    "is_show": 1,
                                    "sid": "4001138",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "电力",
                                    "is_show": 1,
                                    "sid": "4001139",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "冶金",
                                    "is_show": 1,
                                    "sid": "4001140",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "航空航天",
                                    "is_show": 1,
                                    "sid": "4001141",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "机械",
                                    "is_show": 1,
                                    "sid": "4001142",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "商物粮",
                                    "is_show": 1,
                                    "sid": "4001143",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "核工业",
                                    "is_show": 1,
                                    "sid": "4001144",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "电子通信",
                                    "is_show": 1,
                                    "sid": "4001145",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "轻纺",
                                    "is_show": 1,
                                    "sid": "4001146",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "建材",
                                    "is_show": 1,
                                    "sid": "4001147",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "铁道",
                                    "is_show": 1,
                                    "sid": "4001148",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "公路",
                                    "is_show": 1,
                                    "sid": "4001149",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "水运",
                                    "is_show": 1,
                                    "sid": "4001150",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "民航",
                                    "is_show": 1,
                                    "sid": "4001151",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "市政",
                                    "is_show": 1,
                                    "sid": "4001152",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "海洋",
                                    "is_show": 1,
                                    "sid": "4001153",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "水利",
                                    "is_show": 1,
                                    "sid": "4001154",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "农林",
                                    "is_show": 1,
                                    "sid": "4001155",
                                    "pid": "4001136",
                                    "list": []
                                },
                                {
                                    "name": "建筑",
                                    "is_show": 1,
                                    "sid": "4001156",
                                    "pid": "4001136",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "工程勘察",
                            "is_show": 1,
                            "sid": "4001157",
                            "pid": "4000003",
                            "list": [
                                {
                                    "name": "岩土工程",
                                    "is_show": 1,
                                    "sid": "4001158",
                                    "pid": "4001157",
                                    "list": []
                                },
                                {
                                    "name": "水文地质",
                                    "is_show": 1,
                                    "sid": "4001159",
                                    "pid": "4001157",
                                    "list": []
                                },
                                {
                                    "name": "工程测量",
                                    "is_show": 1,
                                    "sid": "4001160",
                                    "pid": "4001157",
                                    "list": []
                                },
                                {
                                    "name": "工程钻探",
                                    "is_show": 1,
                                    "sid": "4001161",
                                    "pid": "4001157",
                                    "list": []
                                },
                                {
                                    "name": "工程凿井",
                                    "is_show": 1,
                                    "sid": "4001162",
                                    "pid": "4001157",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "工程监理",
                            "is_show": 1,
                            "sid": "4001163",
                            "pid": "4000003",
                            "list": [
                                {
                                    "name": "房屋建筑工程",
                                    "is_show": 1,
                                    "sid": "4001164",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "冶炼工程",
                                    "is_show": 1,
                                    "sid": "4001165",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "矿山工程",
                                    "is_show": 1,
                                    "sid": "4001166",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "化工石油工程",
                                    "is_show": 1,
                                    "sid": "4001167",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "水利水电工程",
                                    "is_show": 1,
                                    "sid": "4001168",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "电力工程",
                                    "is_show": 1,
                                    "sid": "4001169",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "农林工程",
                                    "is_show": 1,
                                    "sid": "4001170",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "铁路工程",
                                    "is_show": 1,
                                    "sid": "4001171",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "公路工程",
                                    "is_show": 1,
                                    "sid": "4001172",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "港口与航道工程",
                                    "is_show": 1,
                                    "sid": "4001173",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "航天航空工程",
                                    "is_show": 1,
                                    "sid": "4001174",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "通信工程",
                                    "is_show": 1,
                                    "sid": "4001175",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "市政公用工程",
                                    "is_show": 1,
                                    "sid": "4001176",
                                    "pid": "4001163",
                                    "list": []
                                },
                                {
                                    "name": "机电安装工程",
                                    "is_show": 1,
                                    "sid": "4001177",
                                    "pid": "4001163",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "工程造价咨询",
                            "is_show": 0,
                            "sid": "4001178",
                            "pid": "4000003",
                            "list": [
                                {
                                    "name": "房屋建筑工程",
                                    "is_show": 0,
                                    "sid": "4001179",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "冶炼工程",
                                    "is_show": 0,
                                    "sid": "4001180",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "矿山工程",
                                    "is_show": 0,
                                    "sid": "4001181",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "化工石油工程",
                                    "is_show": 0,
                                    "sid": "4001182",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "水利水电工程",
                                    "is_show": 0,
                                    "sid": "4001183",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "电力工程",
                                    "is_show": 0,
                                    "sid": "4001184",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "农林工程",
                                    "is_show": 0,
                                    "sid": "4001185",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "铁路工程",
                                    "is_show": 0,
                                    "sid": "4001186",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "公路工程",
                                    "is_show": 0,
                                    "sid": "4001187",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "港口与航道工程",
                                    "is_show": 0,
                                    "sid": "4001188",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "航天航空工程",
                                    "is_show": 0,
                                    "sid": "4001189",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "通信工程",
                                    "is_show": 0,
                                    "sid": "4001190",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "市政公用工程",
                                    "is_show": 0,
                                    "sid": "4001191",
                                    "pid": "4001178",
                                    "list": []
                                },
                                {
                                    "name": "机电安装工程",
                                    "is_show": 0,
                                    "sid": "4001192",
                                    "pid": "4001178",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "劳务分包",
                            "is_show": 0,
                            "sid": "4001193",
                            "pid": "4000003",
                            "list": [
                                {
                                    "name": "劳务分包",
                                    "is_show": 0,
                                    "sid": "4001194",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "木工作业",
                                    "is_show": 0,
                                    "sid": "4001195",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "砌筑作业",
                                    "is_show": 0,
                                    "sid": "4001196",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "抹灰作业",
                                    "is_show": 0,
                                    "sid": "4001197",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "油漆作业",
                                    "is_show": 0,
                                    "sid": "4001198",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "钢筋作业",
                                    "is_show": 0,
                                    "sid": "4001199",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "混凝土作业",
                                    "is_show": 0,
                                    "sid": "4001200",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "脚手架作业",
                                    "is_show": 0,
                                    "sid": "4001201",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "模板作业",
                                    "is_show": 0,
                                    "sid": "4001202",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "焊接作业",
                                    "is_show": 0,
                                    "sid": "4001203",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "水暖电安装作业",
                                    "is_show": 0,
                                    "sid": "4001204",
                                    "pid": "4001193",
                                    "list": []
                                },
                                {
                                    "name": "架线作业",
                                    "is_show": 0,
                                    "sid": "4001205",
                                    "pid": "4001193",
                                    "list": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "name": "政府采购",
                    "is_show": 1,
                    "sid": "4000004",
                    "pid": "0",
                    "list": [
                        {
                            "name": "设备类",
                            "is_show": 1,
                            "sid": "4001206",
                            "pid": "4000004",
                            "list": [
                                {
                                    "name": "服务器",
                                    "is_show": 1,
                                    "sid": "4001207",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "台式计算机",
                                    "is_show": 1,
                                    "sid": "4001208",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "台式机",
                                    "is_show": 1,
                                    "sid": "4001209",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "便携式计算机",
                                    "is_show": 1,
                                    "sid": "4001210",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "笔记本电脑",
                                    "is_show": 1,
                                    "sid": "4001211",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "打印机",
                                    "is_show": 1,
                                    "sid": "4001212",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "液晶显示器",
                                    "is_show": 1,
                                    "sid": "4001213",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "扫描仪",
                                    "is_show": 1,
                                    "sid": "4001214",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "基础软件",
                                    "is_show": 1,
                                    "sid": "4001215",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "复印机",
                                    "is_show": 1,
                                    "sid": "4001216",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "投影仪",
                                    "is_show": 1,
                                    "sid": "4001217",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "多功能一体机",
                                    "is_show": 1,
                                    "sid": "4001218",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "LED显示屏",
                                    "is_show": 1,
                                    "sid": "4001219",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "触控一体机",
                                    "is_show": 1,
                                    "sid": "4001220",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "碎纸机",
                                    "is_show": 1,
                                    "sid": "4001221",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "乘用车",
                                    "is_show": 1,
                                    "sid": "4001222",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "客车",
                                    "is_show": 1,
                                    "sid": "4001223",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "专用车辆",
                                    "is_show": 1,
                                    "sid": "4001224",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "电梯",
                                    "is_show": 1,
                                    "sid": "4001225",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "不间断电源",
                                    "is_show": 1,
                                    "sid": "4001226",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "UPS",
                                    "is_show": 1,
                                    "sid": "4001227",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "空调机",
                                    "is_show": 1,
                                    "sid": "4001228",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "家具用具",
                                    "is_show": 1,
                                    "sid": "4001229",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "复印纸",
                                    "is_show": 1,
                                    "sid": "4001230",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "计算机网络设备",
                                    "is_show": 1,
                                    "sid": "4001231",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "被服装具",
                                    "is_show": 1,
                                    "sid": "4001232",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "图书",
                                    "is_show": 1,
                                    "sid": "4001233",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "路由器",
                                    "is_show": 1,
                                    "sid": "4001234",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "交换机",
                                    "is_show": 1,
                                    "sid": "4001235",
                                    "pid": "4001206",
                                    "list": []
                                },
                                {
                                    "name": "防火墙",
                                    "is_show": 1,
                                    "sid": "4001236",
                                    "pid": "4001206",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "服务类",
                            "is_show": 1,
                            "sid": "4001237",
                            "pid": "4000004",
                            "list": [
                                {
                                    "name": "互联网接入服务",
                                    "is_show": 1,
                                    "sid": "4001238",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "车辆维修和保养服务",
                                    "is_show": 1,
                                    "sid": "4001239",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "车辆加油服务",
                                    "is_show": 1,
                                    "sid": "4001240",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "印刷服务",
                                    "is_show": 1,
                                    "sid": "4001241",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "物业管理服务",
                                    "is_show": 1,
                                    "sid": "4001242",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "机动车保险服务",
                                    "is_show": 1,
                                    "sid": "4001243",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "云计算服务",
                                    "is_show": 1,
                                    "sid": "4001244",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "车辆及其他运输机械租赁服务",
                                    "is_show": 1,
                                    "sid": "4001245",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "展览服务",
                                    "is_show": 1,
                                    "sid": "4001246",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "监理服务",
                                    "is_show": 1,
                                    "sid": "4001247",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "造价服务",
                                    "is_show": 1,
                                    "sid": "4001248",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "审计服务",
                                    "is_show": 1,
                                    "sid": "4001249",
                                    "pid": "4001237",
                                    "list": []
                                },
                                {
                                    "name": "资产及其他评估服务",
                                    "is_show": 1,
                                    "sid": "4001250",
                                    "pid": "4001237",
                                    "list": []
                                }
                            ]
                        },
                        {
                            "name": "工程类",
                            "is_show": 1,
                            "sid": "4001251",
                            "pid": "4000004",
                            "list": [
                                {
                                    "name": "装修工程",
                                    "is_show": 1,
                                    "sid": "4001252",
                                    "pid": "4001251",
                                    "list": []
                                },
                                {
                                    "name": "修缮工程",
                                    "is_show": 1,
                                    "sid": "4001253",
                                    "pid": "4001251",
                                    "list": []
                                },
                                {
                                    "name": "拆除工程",
                                    "is_show": 1,
                                    "sid": "4001254",
                                    "pid": "4001251",
                                    "list": []
                                }
                            ]
                        }
                    ]
                }
            ]
