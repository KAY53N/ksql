<?php
$mysqli = new mysqli('127.0.0.1', 'root', '', 'test');
if(mysqli_connect_error())
{
    echo mysqli_connect_error();
}

$mysqli->set_charset("utf8");

$sql = 'SELECT * FROM ksql_article WHERE id="'.$_GET['id'].'" LIMIT 0,1';

//echo $sql.'<hr>';

$query = $mysqli->query($sql);

$article = $query->fetch_assoc();

$mysqli->close();

$token = md5(time().mt_rand(1, 99999).'ABCDEFG');


/* 
	$html = file_get_contents('http://www.xujiantao.com/works/lvsenshop/');

	$url = "http://tool.oschina.net/action/format/html";
	$postData = ['html'=>$html, 'fhtml'=>''];
	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL, $url);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
	curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
	$output = curl_exec($ch);
	curl_close($ch);

	$newHtml = json_decode($output);
	
	echo $newHtml->fhtml;
	exit; */
	

?>
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, user-scalable=1" />
    <title><?php echo $article['title'] ?></title>
    <meta name="keywords" content="iOS" />
    <meta name="description" content="如果你经常使用iPhone预装的信息应用，那么你是否想过给这款应用的聊天界面换一个效果。如果你想尝试的话，越狱社区最近上架的TranslucentMessages插件或许能满足你的要求。TranslucentMessages插件不会更改信息应用中的任何功能，只是改变它的整体...">
    <meta name="TOKEN" content="<?php echo strtoupper($token) ?>">
	<base href="https://news.cnblogs.com">
	<link id="rsslink" title="rss" type="application/rss+xml" rel="alternate" href="http://feed.cnblogs.com/news/rss" />
    <link rel="shortcut icon" href="//common.cnblogs.com/favicon.ico" />
    <link href="/bundles/news.css?v=jQrnQu3jzqklQQvY3N2Eh8je5iDqnyXGXrirrLFP6UM1" rel="stylesheet"/>

    <link rel="stylesheet" type="text/css" href="//mention.cnblogs.com/css/mention-simple.css?id=20160613">
    <link id="smallScreen" rel="stylesheet" type="text/css" media="only screen and (max-width: 768px)" href="/Content/smallScreen.css" />
    <script type="text/javascript" src="//common.cnblogs.com/script/jquery.js"></script>
    <script src="/bundles/news.js?v=K1uUEN-sO9a5OH0YwSC5lvqS0hLXe-Uz_i4kSPmoZo81"></script>

</head>
<body><a name="top"></a><div id="wrap">
        <div id="header">
            <a name="top"></a>
            <div id="wrapper_top_block">
                <div id="login_area">
                </div>
                <div id="top_mini_nav_block">&laquo; <a href="//www.cnblogs.com" class="dark_gray" title="程序员的网上家园">网站首页</a> <a href="http://zzk.cnblogs.com/" class="dark_gray">找找看</a></div>
                <div class="clear"></div>
            </div>
        </div>
    </div>
    <div id="main_wrapper">
        <div id="main_header">
            <div class="header_div">
                <div class="logo">
                    <a href="//www.cnblogs.com"><img src="/images/logo.gif" alt="logo" /></a>
                </div>
                <div class="banner">
                    <div id="clubHeader_panelNews">
                        <div id='ad_e1' style="width:728px;height:90px;"></div>
                    </div>
                </div>
            </div>
            <div class="mainmenu">
                <div class="feedback_block">
                    <a href="//group.cnblogs.com/forum/public/">反馈问题或建议</a>
                </div>
                <ul id="navlist_main">
                    <li style="margin-left:20px;"><a href="//www.cnblogs.com">首页</a></li>
                    <li>
                        <a href="//home.cnblogs.com">园子</a>
                    </li>
                    <li>
                    </li>
                    <li id="clubHeader_liNews">
                        <a id="clubHeader_lnkNews" title="IT新闻" class="current" href="/">新 闻</a>
                    </li>
                    <li>
                        <a id="clubHeader_lkQuestionMenu" href="//q.cnblogs.com/">博问</a>
                    </li>
                    <li>
                    </li>
                    <li>
                        <a id="clubHeader_lkIngMenu" href="//ing.cnblogs.com/">闪存</a>
                    </li>
                    <li>
                        <a id="clubHeader_lnkWz" href="//wz.cnblogs.com/">收藏</a>
                    </li>
                    <li>
                        <a href="//job.cnblogs.com">招聘</a>
                    </li>
                    <li>
                        <a href="//kb.cnblogs.com">知识库</a>
                    </li>
                    <li id="clubHeader_liMyMessage">
                    </li>
                </ul>
            </div>
            <script type="text/javascript">
                if (typeof (jQuery) != 'undefined') {
                    GetUserInfo();
                }
            </script>
            
        </div>
        

<div id="sideleft">
	<div id="guide">
		<h3>
			<a href="//www.cnblogs.com" title="程序员的网上家园">博客园</a> » <a href="//news.cnblogs.com" title="IT新闻">新闻</a>
 » <a href="/n/topic_82.htm">Apple</a>
		</h3>
	</div>
	<div id="news_main">
		<div id="news_title"><a href="//news.cnblogs.com/n/563271/"><?php echo $article['title'] ?></a></div>
		<div id="news_info">
			<span class="news_poster">投递人 <a href="//home.cnblogs.com/u/34358/">itwriter</a></span>
			<span class="time">发布于 2017-02-20 13:12</span>
			<span class="comment"><a href="/n/563271/#comment" id="News_CommentCount_Head"></a></span>
			<span class="view" id="News_TotalView"></span>
				<a id="link_source1" class="wz" target="_blank" href="http://www.feng.com/iPhone/news/2017-02-19/Be-great-_670258.shtml">原文链接</a>
			<a href="#" onclick="PutInWz();return false;" class="wz">[收藏]</a>
			<a id="HeadPreNewsId" href="#" class="gray" title="上一篇">«</a> <a id="HeadNextNewsId" href="#" class="gray" title="下一篇">»</a>
		</div><!--end: news_info -->
		<div id="news_content">
			<div id="news_body">
			<?php echo $article['content'] ?>
			</div><!--end: news_body -->
			<div id="news_otherinfo">
				<div id="up_down">
					<div class="diggit" onclick="VoteNews(563271,'agree')">
						<span class="diggnum" id="digg_num_563271"></span>
					</div>
					<div class="buryit" onclick="VoteNews(563271,'anti')">
						<span class="burynum" id="bury_num_563271"></span>
					</div>
					<div class="clear"></div>
					<div id="digg_tip_563271" class="digg_tip_detail">&nbsp;</div>
				</div>
				<div id="come_from">
						来自:
											<a id="link_source2" target="_blank" href="http://www.feng.com/iPhone/news/2017-02-19/Be-great-_670258.shtml">www.feng.com</a>
				</div><!--end: come_from -->
				<div class="clear"></div>
				<div id="article_A4area">
					<span id="shareA4" class="fl">
						<a href="http://www.cnblogs.com/cmt/p/udacity.html" target="_blank"><b>Udacity 博客园专属学费优惠</b></a>
					</span>
					<span id="sharebox">
						<a rel="nofollow" onclick="ShareToTsina();return false;" href="javascript:void(0)"><img border="0" title="转发至新浪微博" src="/images/icon_sina.gif" alt="新浪微博"></a>
						<a rel="nofollow" onclick="ShareToTweixin();return false;" href="javascript:void(0)"><img border="0" title="分享至微信" src="/images/icon_weixin.gif" alt="分享至微信"></a>
					</span>
					<div class="clear">
					</div>
				</div><!--end: share block-->
				<div class="clear"></div>
				<div id="news_more_info">
						<div class="news_tags">标签：  <a href="/n/tag/iOS/" class="catalink">iOS</a></div>
                    <input type="hidden" name="tagsId" id="tagsId" value="iOS" />
				</div>
			</div><!--end: news_otherinfo -->
		</div><!--end: news_content 新闻的主体 -->
		<div class="prevnext_block">
			<div id="FootPreNewsId">
			</div>
			<div id="FootNextNewsId" style="margin-top:5px;">
			</div>
		</div>
		<div id="comment_tips">
		</div>
		<input type="hidden" value="563271" id="lbContentID">
		<a name="comment"></a>
		<div id="comment_main">
			<div id="comment_main_list">
			</div>
			<div style="text-align:right"><a href="javascript:void(0);" onclick="GetNewsComment(563271);" class="gray">刷新评论</a></div>
		</div>
		<!--end: comment_main -->
		<!-- 评论结束 -->
		<span id="Comment_new"></span><span id="Comment_Edit_ID"></span>
		<a name="bottom"></a>
		<div id="comment_form_block" class="qitem_reply">
        </div>
        <span style="display:none" id="ReplyToCommentId">0</span>
    </div>
</div>
<script src="/bundles/news_detail.js?v=1Ll5ZaRZ-pVExg0-jS8BqcCmMutoPZH3_mTolm0zyZs1"></script>

<script type='text/javascript' src="//mention.cnblogs.com/bundles/mention.js?id=20160615-2"></script>
<script type="text/javascript">
	var ContentID = 563271;
	var commentCount=0;
	$(function () {
		CommonLoadNews("/NewsAjax/GetRecentNews", "RecentNewsId", 7);
		CommonLoadNews("/NewsAjax/GetHotNewsByViewCount", "HotNewsId", 7);
		LoadPreNextNewsByContentId(563271);
	    GetRelativeNews("RelativeNewsId",563271,$("#tagsId").val(),7);
		GetNewsComment(563271);
	    LoadAjaxNewsInfo(563271);
	    LoadDetailommentInfo();
		LoadHotComments(563271,0);
		setTimeout(function () { incrementViewCount(563271); }, 200);
	});
</script>
        <div id="sideright">
            <script async='async' src='//www.googletagservices.com/tag/js/gpt.js'></script>
            <script>
                var googletag = googletag || {};
                googletag.cmd = googletag.cmd || [];
            </script>
            <script>
                googletag.cmd.push(function () {
                    googletag.defineSlot('/1090369/news_E2', [300, 250], 'div-gpt-ad-1471056911903-0').addService(googletag.pubads());
                    googletag.pubads().enableSingleRequest();
                    googletag.enableServices();
                });
            </script>
            
    <div id="side_right_search">
        <input type="text" id="google_search_q" size="27" class="side_right_search_q" onkeydown="return google_search_enter(event);">
		<input type="submit" name="sa" value="搜索新闻" class="side_right_search_sa" onclick="return google_search();">
	</div>
<div class="side_block">
    <div class="a4content">
        <div id='div-gpt-ad-1471056911903-0' style='height:250px; width:300px;'>
            <script>
                googletag.cmd.push(function () { googletag.display('div-gpt-ad-1471056911903-0'); });
            </script>
        </div>
    </div>
</div>

	<div id="side-ad-text" class="side-ad-text" style="height: auto;">
	</div>
	<div id="hot_comment_block" class="side_block" style="display:none;">
		<h3 class="title_red">热门评论</h3>
		<ul class="block_list" id="best_comment"></ul>
	</div>
	<div class="side_block">
		<h3 class="title_yellow">24小时阅读排行</h3>
		<ul class="topnews block_list bt" id="HotNewsId"></ul>
	</div>
	<div class="side_block">
		<h3 class="title_green">最新新闻</h3>
		<ul class="topnews block_list bt" id="RecentNewsId"></ul>
	</div>
<div class="side_block">
    <div id="ad_e3" style="height:250px; width:300px;"></div>
</div>

	<div id="job_recommend" style="display:none">
		<h3 class="title_yellow">推荐职位</h3>
		<ul id="job_recommend_list" class="topnews block_list bt">
			<li></li>
		</ul>
	</div>
	<div id="relative_news" class="side_block">
		<h3 class="title_blue">相关新闻</h3>
		<ul class="topnews block_list bt" id="RelativeNewsId"></ul>
	</div>

        </div>
        <div class="clear">
        </div>
        <div id="goTop">
            <a href="#top"><img src="/images/ico_top.gif" alt="回到页首" title="回到页首 Top" /></a>
        </div>
        <div id="footer">
            <div id="foot">
                <a href="//www.cnblogs.com/AboutUS.aspx">关于博客园</a><a href="//www.cnblogs.com/ContactUs.aspx">联系我们</a><a href="//www.cnblogs.com/ad.aspx">广告服务</a><span>&copy;2004-2017</span><a href="//www.cnblogs.com">博客园</a>合作伙伴：<a href="http://www.hujiang.com" target="_blank">沪江网</a>
            </div>
            <div id="footMobile" style="display:none;">
                <span>&copy;2004-2017</span>&nbsp;<a href="//www.cnblogs.com">博客园</a>
            </div>
        </div>
        <script type="text/javascript">
            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-476124-8']);
            _gaq.push(['_trackPageview']);
            (function () {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();
        </script>
    </div>
</body>
</html>
