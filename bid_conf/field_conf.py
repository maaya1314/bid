

class FieldConf(object):
    # 字段
    uuid = 'uuid'  # 唯一业务id，对url做md5取值
    article_url = 'article_url'  # 链接
    title = '标题'  # 标题
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
        'primary_indicators': '一级指标',
        'secondary_indicators': '二级指标',
        'source_code': '源码',
        'channel': '所属频道'
    }
