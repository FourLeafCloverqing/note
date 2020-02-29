# 正则表达式 :re
# 正则用来匹配字符串中的内容,
# 找个视频看吧

###正则表达的理解即为从一个文档中找到相应的词、数字，当不确定是啥可以用.*?，用()说明输出内容。
###import re  re.findall()  .*?：泛匹配，  .*：精确匹配

# a = 'hello 12341232135, hello aaa'

###正则表达
#test1.1：从一篇英文诗中找到所有的to单词，
# def reg_exp_words():
#     import re
#     poem_1 =open('poem.txt','r')
#     content =poem_1.read()
    # print(content)
    # poem_1.close()
    # result = re.findall('to',content)#将content中所有只要带to就输出，其中包括出现在一个单词中。
    # result = re.findall(' to ',content)#将content 中的前后各一个空格，输出to这个单词
#     print(result)
#     print(len(result))
# reg_exp_words()

#test1.2:从文档中找到所有的以a开头且字母个数为3个的所有单词
# def reg_exp_words():
#     poem_2 = open('poem.txt','r')
#     content = poem_2.read()
#     poem_2.close()
#     import re
#     result =re.findall(' (a[a-z][a-z]) |(A[a-z][a-z]) ',content)
#     final_result = set()
#     for pair in result:
#         if pair[0] not in final_result:
#             final_result.add(pair[0])
#         if pair[1] not  in final_result:
#             final_result.add(pair[1])
#     final_result.remove('')
#
#     print(final_result)

    # result = re.findall('a..',content)
    # result = re.findall('[Aa] \d{2}',content)
    # result = re.findall(' *[Aa][a-z][a-z]',content)#空格*代表既可以有空格 也可以没有空格  空格*代表空字符串、一个a，两个a，等待多个a
    # print(result)
    # print(len(result))
    # print(set(result))


#test2:从百度贴吧网页中匹配出所有的发布时间
# def time():
#     txt = '''
#     吧主公告（关于物联网卡整顿）czhaol
# 51
#  作为新任吧主，首先感谢大家的支持！其次，希望大家不要发不良信czhaol
# 2
# 博士物联卡管理系统可对接多个平台kangsgo
# 博士物联管理平台在不断开发中，提供贴心的售后以及丰富的教程资料。目前已有功能为: 卡板管理，实名管理，佣金管理，代理管理（无限开代理），用户管理，菜单设置，订购管理 目前正在开发功能有: 公告管理，佣金管理，卡密管理，秒反佣金，工单管理 下一步计划开发功能有: 卡板限速，轮询 V：billvmiot 以下是预览截图
# 共 6 张 流量搬运...16:12
# 0
# 人脸识别测温SAAS系统贴吧用户_...
# 抗击疫情，我们在行动。针对以上现状的痛点难点，慧睿思通调动自身的研发力量，以
# 科技之力抗“疫”，对原有产品进行升级优化，推出不同场景的人脸识别加测温管控，有效实现办公楼写字楼 社区出入口等场景下的无接触智能体温检测、高效率通行、智能预警的目的，大幅提高测温效率和异常体温者检出的准确率，有效减少交叉感染风险，切实实现了防疫“属地化 网络化和信息化”管理。
#  贴吧用户_...16:29
# 0
# 就问你6元一台云虚拟主机,心动不？百度智能云广告
# 贴吧图片
# 721
# 最新物联网小白到精通超级梦想9...
# 共 8 张 N9y35N9SO6A016:31
# 0
# 遇见YJL短视频~☝1、每天签到赚：4元🔥2、看视频：3元壹曲江湖酒
# 遇见YJL短视频~ ☝1、每天签到赚：4元 🔥2、看视频：3元 3、分享朋友圈：5元 🌴4、发布短视频：2元 💰每天花几分钟，必赚14元 🐳心动不如行动，抓住机会，你就是网赚小能手 ＋V:2191127891
#  壹曲江湖酒10:37
# 26
# 秉性物联 稳定服务商有能力欢迎咨询有情终会...
# 秉性物联 稳定服务商 有能力欢迎咨询
#  428b9LND9716:28
# 6
# 举报图片所述几个贴吧吧主，私下谋利，一个人控制了七个贴吧。我明号科技
# 举报图片所述几个贴吧吧主，私下谋利，一个人控制了七个贴吧。我可以提供强有力的证据，望百度贴吧工作人员核实，创造一个良好的贴吧环境。
#  明号科技13:42
# 721
# 2019物联网小白到精通的分享和平版花花
# 共 9 张 N9y35N9SO6A015:45
# 49
# 金源通讯，诚招一级代理 支持全国零售，批发等合作代理0门槛，金源通讯
# 金源通讯，诚招一级代理 支持全国零售，批发等合作 代理0门槛，卡板稳，不死卡，高返利，可提供卡板测试 ———————————— <动态IP，超低延迟，全程4G> 适合工作室，学生党，游戏专用 期待与各大超市，网吧，商店共同合作 ———————————— 欢迎大小代理来撩 ————————————
#  金源通讯15:44
# 0
# 6元购买百度智能云高稳定虚拟机咋申请?百度智能云广告
# 贴吧图片
# 0
# 移动流量卡，为稳定而生，欢迎有需求的朋友联系，拒绝暴利！广西流量搬运...
# 移动流量卡，为稳定而生，欢迎有需求的朋友联系，拒绝暴利！广西新疆云南暂时没服务，其他地区正常使用
#  流量搬运...15:37
# 5
# 各类小程序制作，游戏搭建，现招代理中越传媒...
# 各类小程序制作，游戏搭建，现招代理 诚信搭建: 1.股配 2.科创版融资融卷 3.数字货币 4.MT4 5.国内外期货 wechat：ye190314
#  中越传媒...15:36
# 30
# 垃圾亿享物联网卡，骗子公司，卖的卡都不能用，还不给退。衡阳市海月明者
# 垃圾亿享物联网卡，骗子公司，卖的卡都不能用，还不给退。衡阳市亿享物联网科技有限公司。还有湖南智行天下物联网科技有限公司，骗子公司
#  沐艺科技
#     '''
#     import re
#     result = re.findall('[1-9][1-9]:[1-9][1-9]',txt)
#     print(result)
# time()

#test3：从一个猫眼电影网页中找到各个电影的名称、上映时间、主演、评分
# def maoyan():
#     txt = '''
#    <!DOCTYPE html>
#
# <!--[if IE 8]><html class="ie8"><![endif]-->
# <!--[if IE 9]><html class="ie9"><![endif]-->
# <!--[if gt IE 9]><!--><html><!--<![endif]-->
# <head>
#   <title>热映口碑榜 - 猫眼电影 - 一网打尽好电影</title>
#
#   <link rel="dns-prefetch" href="//p0.meituan.net"  />
#   <link rel="dns-prefetch" href="//p1.meituan.net"  />
#   <link rel="dns-prefetch" href="//ms0.meituan.net" />
#   <link rel="dns-prefetch" href="//s0.meituan.net" />
#   <link rel="dns-prefetch" href="//ms1.meituan.net" />
#   <link rel="dns-prefetch" href="//analytics.meituan.com" />
#   <link rel="dns-prefetch" href="//report.meituan.com" />
#   <link rel="dns-prefetch" href="//frep.meituan.com" />
#
#
#   <meta charset="utf-8">
#   <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
#   <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
#   <meta http-equiv="cleartype" content="yes" />
#   <meta http-equiv="X-UA-Compatible" content="IE=edge" />
#   <meta name="renderer" content="webkit" />
#
#   <meta name="HandheldFriendly" content="true" />
#   <meta name="format-detection" content="email=no" />
#   <meta name="format-detection" content="telephone=no" />
#   <meta name="viewport" content="width=device-width, initial-scale=1">
#
#
#   <script>"use strict";!function(){var i=0<arguments.length&&void 0!==arguments[0]?arguments[0]:"_Owl_",n=window;n[i]||(n[i]={isRunning:!1,isReady:!1,preTasks:[],dataSet:[],use:function(i,t){this.isReady&&n.Owl&&n.Owl[i](t),this.preTasks.push({api:i,data:[t]})},add:function(i){this.dataSet.push(i)},run:function(){var t=this;if(!this.isRunning){this.isRunning=!0;var i=n.onerror;n.onerror=function(){this.isReady||this.add({type:"jsError",data:arguments}),i&&i.apply(n,arguments)}.bind(this),(n.addEventListener||n.attachEvent)("error",function(i){t.isReady||t.add({type:"resError",data:[i]})},!0)}}},n[i].run())}();</script>
#   <script>
#   cid = "c_wx6zb55";
#   ci = 763;
# val = {"subnavId":7};    window.system = {};
#
#   window.openPlatform = '';
#   window.openPlatformSub = '';
#   window.$mtsiFlag = '0';
#
#   </script>
#   <link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.d1d257d3.css"/>
# <link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.92a06072.css"/>
#   <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/stat.88d57c80.js"></script>
#   <script>if(window.devicePixelRatio >= 2) { document.write('<link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image-2x.8ba7074d.css"/>') }</script>
#   <style>
#     @font-face {
#       font-family: stonefont;
#       src: url('//vfile.meituan.net/colorstone/26c1913af9ff774487f63e76543acc723432.eot');
#       src: url('//vfile.meituan.net/colorstone/26c1913af9ff774487f63e76543acc723432.eot?#iefix') format('embedded-opentype'),
#            url('//vfile.meituan.net/colorstone/a6dff641da78b7d825d4fcc7e6b6bf442268.woff') format('woff');
#     }
#
#     .stonefont {
#       font-family: stonefont;
#     }
#   </style>
#   <script>
#   var _hmt = _hmt || [];
#   (function() {
#   var hm = document.createElement("script");
#   hm.src = "https://hm.baidu.com/hm.js?703e94591e87be68cc8da0da7cbd0be2";
#   var s = document.getElementsByTagName("script")[0];
#   s.parentNode.insertBefore(hm, s);
#   })();
#   </script>
# </head>
# <body>
#
#
# <div class="header">
#   <div class="header-inner">
#           <a href="//maoyan.com" class="logo" data-act="icon-click"></a>
#         <div class="city-container" data-val="{currentcityid:763 }">
#             <div class="city-selected">
#                 <div class="city-name">
#                   永年
#                   <span class="caret"></span>
#                 </div>
#             </div>
#             <div class="city-list" data-val="{ localcityid: 763 }">
#                 <div class="city-list-header">定位城市：<a class="js-geo-city" data-ci="763">永年</a></div>
#
#             </div>
#         </div>
#
#
#         <div class="nav">
#             <ul class="navbar">
#                 <li><a href="/" data-act="home-click"  >首页</a></li>
#                 <li><a href="/films" data-act="movies-click" >电影</a></li>
#                 <li><a href="/cinemas" data-act="cinemas-click" >影院</a></li>
#                 <li><a href="http://www.gewara.com">演出</a></li>
#
#                 <li><a href="/board" data-act="board-click"  class="active" >榜单</a></li>
#                 <li><a href="/news" data-act="hotNews-click" >热点</a></li>
#                 <li><a href="/edimall"  >商城</a></li>
#             </ul>
#         </div>
#
#         <div class="user-info">
#             <div class="user-avatar J-login">
#               <img src="https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
#               <span class="caret"></span>
#               <ul class="user-menu no-login-menu">
#                 <li><a href="javascript:void 0">登录</a></li>
#               </ul>
#             </div>
#         </div>
#
#         <form action="/query" target="_blank" class="search-form" data-actform="search-click">
#             <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
#             <input class="submit" type="submit" value="">
#         </form>
#
#         <div class="app-download">
#           <a href="/app" target="_blank">
#             <span class="iphone-icon"></span>
#             <span class="apptext">APP下载</span>
#             <span class="caret"></span>
#             <div class="download-icon">
#                 <p class="down-title">扫码下载APP</p>
#                 <p class='down-content'>选座更优惠</p>
#             </div>
#           </a>
#         </div>
#
#   </div>
# </div>
# <div class="header-placeholder"></div>
#
# <div class="subnav">
#   <ul class="navbar">
#     <li>
#       <a data-act="subnav-click" data-val="{subnavClick:7}"
#           data-state-val="{subnavId:7}"
#           class="active" href="javascript:void(0);"
#       >热映口碑榜</a>
#     </li>
#     <li>
#       <a data-act="subnav-click" data-val="{subnavClick:6}"
#           href="/board/6"
#       >最受期待榜</a>
#     </li>
#     <li>
#       <a data-act="subnav-click" data-val="{subnavClick:1}"
#           href="/board/1"
#       >国内票房榜</a>
#     </li>
#     <li>
#       <a data-act="subnav-click" data-val="{subnavClick:2}"
#           href="/board/2"
#       >北美票房榜</a>
#     </li>
#     <li>
#       <a data-act="subnav-click" data-val="{subnavClick:4}"
#           href="/board/4"
#       >TOP100榜</a>
#     </li>
#   </ul>
# </div>
#
#
#     <div class="container" id="app" class="page-board/index" >
#
# <div class="content">
#     <div class="wrapper">
#         <div class="main">
#             <p class="update-time">2020-02-21<span class="has-fresh-text">已更新</span></p>
#             <p class="board-content">榜单规则：将昨日国内热映的影片，按照评分从高到低排列取前10名，每天上午10点更新。相关数据来源于“猫眼专业版”及“猫眼电影库”。</p>
#             <dl class="board-wrapper">
#                 <dd>
#                         <i class="board-index board-index-1">1</i>
#     <a href="/films/1277939" title="我和我的祖国" class="image-link" data-act="boarditem-click" data-val="{movieId:1277939}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.meituan.net/moviemachine/b2c5c74d33e45745fd3462e44b3698e18336620.jpg@160w_220h_1e_1c" alt="我和我的祖国" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1277939" title="我和我的祖国" data-act="boarditem-click" data-val="{movieId:1277939}">我和我的祖国</a></p>
#         <p class="star">
#                 主演：黄渤,张译,韩昊霖
#         </p>
# <p class="releasetime">上映时间：2019-09-30</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">7</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-2">2</i>
#     <a href="/films/1190122" title="叶问4：完结篇" class="image-link" data-act="boarditem-click" data-val="{movieId:1190122}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.meituan.net/movie/a3d6ca3bdd5b0ddd7016acff9a9f2f2e2805813.jpg@160w_220h_1e_1c" alt="叶问4：完结篇" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1190122" title="叶问4：完结篇" data-act="boarditem-click" data-val="{movieId:1190122}">叶问4：完结篇</a></p>
#         <p class="star">
#                 主演：甄子丹,吴樾,吴建豪
#         </p>
# <p class="releasetime">上映时间：2019-12-20</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">4</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-3">3</i>
#     <a href="/films/1281095" title="紫罗兰永恒花园 外传：永远与自动手记人偶" class="image-link" data-act="boarditem-click" data-val="{movieId:1281095}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.meituan.net/movie/37e835fdaf68e48dd002b6757374251d6793835.jpg@160w_220h_1e_1c" alt="紫罗兰永恒花园 外传：永远与自动手记人偶" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1281095" title="紫罗兰永恒花园 外传：永远与自动手记人偶" data-act="boarditem-click" data-val="{movieId:1281095}">紫罗兰永恒花园 外传：永远与自动手记人偶</a></p>
#         <p class="star">
#                 主演：石川由依,茅原实里,远藤绫
#         </p>
# <p class="releasetime">上映时间：2020-01-10</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-4">4</i>
#     <a href="/films/1206829" title="音乐家" class="image-link" data-act="boarditem-click" data-val="{movieId:1206829}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p1.meituan.net/movie/b88fe92134056eed2390d3f7009c18792940728.jpg@160w_220h_1e_1c" alt="音乐家" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1206829" title="音乐家" data-act="boarditem-click" data-val="{movieId:1206829}">音乐家</a></p>
#         <p class="star">
#                 主演：胡军,袁泉,别里克·艾特占诺夫
#         </p>
# <p class="releasetime">上映时间：2019-05-17</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-5">5</i>
#     <a href="/films/246083" title="捉妖记" class="image-link" data-act="boarditem-click" data-val="{movieId:246083}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.meituan.net/movie/79182a20224ebe1751b2d8980420cf21149653.jpg@160w_220h_1e_1c" alt="捉妖记" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/246083" title="捉妖记" data-act="boarditem-click" data-val="{movieId:246083}">捉妖记</a></p>
#         <p class="star">
#                 主演：白百何,井柏然,姜武
#         </p>
# <p class="releasetime">上映时间：2015-07-16</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-6">6</i>
#     <a href="/films/1217236" title="悲伤逆流成河" class="image-link" data-act="boarditem-click" data-val="{movieId:1217236}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p1.meituan.net/movie/e27ff51791134dc9cfd72417af9049af197718.jpg@160w_220h_1e_1c" alt="悲伤逆流成河" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1217236" title="悲伤逆流成河" data-act="boarditem-click" data-val="{movieId:1217236}">悲伤逆流成河</a></p>
#         <p class="star">
#                 主演：赵英博,任敏,辛云来
#         </p>
# <p class="releasetime">上映时间：2018-09-21</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-7">7</i>
#     <a href="/films/247300" title="唐人街探案" class="image-link" data-act="boarditem-click" data-val="{movieId:247300}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.meituan.net/moviemachine/905f799a205718d7ede9179b227bfcc99059007.jpg@160w_220h_1e_1c" alt="唐人街探案" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/247300" title="唐人街探案" data-act="boarditem-click" data-val="{movieId:247300}">唐人街探案</a></p>
#         <p class="star">
#                 主演：王宝强,刘昊然,陈赫
#         </p>
# <p class="releasetime">上映时间：2015-12-31</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-8">8</i>
#     <a href="/films/1279731" title="宠爱" class="image-link" data-act="boarditem-click" data-val="{movieId:1279731}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.meituan.net/moviemachine/36eda496688542263d9a0f02ac728327823369.jpg@160w_220h_1e_1c" alt="宠爱" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1279731" title="宠爱" data-act="boarditem-click" data-val="{movieId:1279731}">宠爱</a></p>
#         <p class="star">
#                 主演：于和伟,吴磊,张子枫
#         </p>
# <p class="releasetime">上映时间：2019-12-31</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">8.</i><i class="fraction">9</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-9">9</i>
#     <a href="/films/1215605" title="速度与激情：特别行动" class="image-link" data-act="boarditem-click" data-val="{movieId:1215605}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p1.meituan.net/movie/648bbced128324a4b4ccf7db6c564a251744344.jpg@160w_220h_1e_1c" alt="速度与激情：特别行动" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1215605" title="速度与激情：特别行动" data-act="boarditem-click" data-val="{movieId:1215605}">速度与激情：特别行动</a></p>
#         <p class="star">
#                 主演：道恩·强森,杰森·斯坦森,伊德瑞斯·艾尔巴
#         </p>
# <p class="releasetime">上映时间：2019-08-23</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">8.</i><i class="fraction">6</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#                 <dd>
#                         <i class="board-index board-index-10">10</i>
#     <a href="/films/1132494" title="生存家族" class="image-link" data-act="boarditem-click" data-val="{movieId:1132494}">
#       <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
#       <img data-src="https://p0.meituan.net/movie/5e11cb58b3208861307de8d4704704e5243539.jpg@160w_220h_1e_1c" alt="生存家族" class="board-img" />
#     </a>
#     <div class="board-item-main">
#       <div class="board-item-content">
#               <div class="movie-item-info">
#         <p class="name"><a href="/films/1132494" title="生存家族" data-act="boarditem-click" data-val="{movieId:1132494}">生存家族</a></p>
#         <p class="star">
#                 主演：小日向文世,深津绘里,泉泽祐希
#         </p>
# <p class="releasetime">上映时间：2018-06-22</p>    </div>
#     <div class="movie-item-number score-num">
# <p class="score"><i class="integer">8.</i><i class="fraction">5</i></p>
#     </div>
#
#       </div>
#     </div>
#
#                 </dd>
#             </dl>
#
#         </div>
#     </div>
# </div>
#
#     </div>
#
# <div class="footer">
#   <p class="friendly-links">
#     关于猫眼 :
#     <a href="http://ir.maoyan.com/s/index.php#pageScroll0" target="_blank">关于我们</a>
#     <span></span>
#     <a href="http://ir.maoyan.com/s/index.php#pageScroll1" target="_blank">管理团队</a>
#     <span></span>
#     <a href="http://ir.maoyan.com/s/index.php#pageScroll2" target="_blank">投资者关系</a>
#     &nbsp;&nbsp;&nbsp;&nbsp;
#     友情链接 :
#     <a href="http://www.meituan.com" data-query="utm_source=wwwmaoyan" target="_blank">美团网</a>
#     <span></span>
#     <a href="http://www.gewara.com" data-query="utm_source=wwwmaoyan">格瓦拉</a>
#     <span></span>
#     <a href="http://i.meituan.com/client" data-query="utm_source=wwwmaoyan" target="_blank">美团下载</a>
#     <span></span>
#     <a href="https://www.huanxi.com" data-query="utm_source=maoyan_pc" target="_blank">欢喜首映</a>
#   </p>
#   <p class="friendly-links">
#     商务合作邮箱：v@maoyan.com
#     客服电话：10105335
#     违法和不良信息举报电话：4006018900
#   </p>
#   <p class="friendly-links">
#     用户投诉邮箱：tousujubao@meituan.com
#     舞弊线索举报邮箱：wubijubao@maoyan.com
#   </p>
#   <p class="friendly-links  credentials">
#     <a href="/about/licence/1" target="_blank">中华人民共和国增值电信业务经营许可证 京B2-20190350</a>
#     <span></span>
#     <a href="/about/licence/4" target="_blank">营业性演出许可证 京演（机构）（2019）4094号</a>
#   </p>
#   <p class="friendly-links  credentials">
#     <a href="/about/licence/3" target="_blank">广播电视节目制作经营许可证 （京）字第08478号</a>
#     <span></span>
#     <a href="/about/licence/2" target="_blank">网络文化经营许可证 京网文（2019）3837-369号 </a>
#   </p>
#   <p class="friendly-links  credentials">
#     <a href="/rules/agreement" target="_blank">猫眼用户服务协议 </a>
#     <span></span>
#     <a href="/rules/rule" target="_blank">猫眼平台交易规则总则 </a>
#     <span></span>
#     <a href="/rules/privacy" target="_blank">隐私政策 </a>
#   </p>
#   <p class="friendly-links  credentials">
#     <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232" target="_blank">京公网安备
#       11010102003232号</a>
#     <span></span>
#     <a href="http://www.beian.miit.gov.cn/" target="_blank">京ICP备16022489号</a>
#   </p>
#   <p>北京猫眼文化传媒有限公司</p>
#   <p>
#     &copy;2016
#     猫眼电影 maoyan.com</p>
#   <div class="certificate">
#     <a href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/350CF8BCA8416C4FE0530140A8C0957E"
#       target="_blank">
#       <img src="http://p0.meituan.net/moviemachine/e54374ccf134d1f7b2c5b075a74fca525326.png" />
#     </a>
#     <a href="/about/licence/5" target="_blank">
#       <img src="http://p1.meituan.net/moviemachine/805f605d5cf1b1a02a4e3a5e29df003b8376.png" />
#     </a>
#   </div>
# </div>
#
#     <script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl_1.7.11.js"></script>
#     <script>
#       Owl.start({
#         project: 'com.sankuai.movie.fe.mywww',
#         pageUrl: location.href.split('?')[0].replace(/\/\d+/g, '/:id'),
#         devMode: false
#       })
#     </script>
#     <script src="//s0.meituan.net/bs/?f=myfe/canary:mojo-0.1.2.js"></script>
#     <script>
#       MAInit({
#         appkey: 'com.sankuai.movie.fe.mywww',
#         app_name: 'maoyan-pc-web',
#         app_version: '1.0.0',
#       })
#     </script>
#     <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-shim.bbad933f.js"></script><![endif]-->
#     <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-sham.d6ea26f4.js"></script><![endif]-->
#     <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.74858235.js"></script>
# <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.e144d497.js"></script>
# </body>
# </html>
#
#     '''
#     import re
#     result = re.findall('title="(.*?)".*?(主演：.*?)\n.*?(上映时间：.*?)</p>.*?(\d\.).*?(\d)</i>',txt,re.S)
#     for i in result:
#         print(i)
    # print(result)

#           < p
#
#     class ="name" > < a href="/films/1277939" title="我和我的祖国" data-act="boarditem-click" data-val="{movieId:1277939}" > 我和我的祖国 < / a > < / p >
#
#     < p
#
#     class ="star" >
#
#     主演：黄渤, 张译, 韩昊霖
#
# < / p >
# < p
#
#
# class ="releasetime" > 上映时间：2019-09-30 < / p > < / div >

# < div
#
#
# class ="movie-item-number score-num" >
#
# < p
#
#
# class ="score" > < i class ="integer" > 9. < / i > < i class ="fraction" > 7 < / i > < / p >
# maoyan()
