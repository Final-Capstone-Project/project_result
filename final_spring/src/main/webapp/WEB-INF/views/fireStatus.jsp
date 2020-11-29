<%@ page session="false"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<style type="text/css">
.statusTitle {
	text-align: center;
	color: darkgreen;
}

.imgcontainer .image {
	background-color: white;
	width: 33.33%;
	float: left;
}

.imgcontainer img {
	background-color: white;
	width: calc(100% - ( 20px * 2));
	margin: 20px;
}
</style>
<%@ include file="/WEB-INF/views/top.jsp"%>
<br>
<h2 class="statusTitle" text-align="center">
	<b>서울시 세부 화재 현황 도표</b>
</h2>
<div class="container">
	<script>
		function img_change(f) {
			var chimg = '<img src="' + $(f).find('option:selected').data('src')
					+ '">';
			$('#change_img').html(chimg);
		}
	</script>
	<div class="text-center">
		<form name="search">
			<select id="fireStatus" onchange="img_change(this);"
				class="btn btn-light dropdown-toggle">
				<option>항목 선택</option>
				<optgroup label="주요 순위">
					<option value="indi_p_top_10"
						data-src="resources/static/images/rank/individual_person_top10.PNG">인명피해
						화재 top10</option>
					<option value="indi_m_top_10"
						data-src="resources/static/images/rank/individual_money_top10.PNG">재산피해
						화재 top10</option>
					<option value="dong_p_top_10"
						data-src="resources/static/images/rank/dong_person_top10.PNG">동별
						인명피해 top10</option>
					<option value="dong_m_top_10"
						data-src="resources/static/images/rank/dong_fire_top10.PNG">동별
						화재발생 top10</option>
				</optgroup>
				<optgroup label="월별">
					<option value="mon"
						data-src="resources/static/images/monthes/month.PNG">월별
						화재</option>
				</optgroup>
				<optgroup label="연도별">
					<option value="year"
						data-src="resources/static/images/years/year.PNG">연도별 화재</option>
				</optgroup>
				<optgroup label="시간대별">
					<option value="t_per_fire"
						data-src="resources/static/images/times/time_per_fire.PNG">발생건수</option>
					<option value="t_per_damage"
						data-src="resources/static/images/times/time_per_damage.PNG">인명피해</option>
				</optgroup>
				<optgroup label="구별">
					<option value="occur"
						data-src="resources/static/images/gu/occur.jpg">발생 현황</option>
					<option value="money_damage"
						data-src="resources/static/images/gu/money_damage.jpg">피해액
						현황</option>
					<option value="human_damage"
						data-src="resources/static/images/gu/human_damage.jpg">사망
						및 부상</option>
				</optgroup>
				<optgroup label="기타">
					<option value="place"
						data-src="resources/static/images/etc/place.PNG">장소별</option>
					<option value="missing"
						data-src="resources/static/images/etc/missing.PNG">오인출동별</option>
					<option value="house"
						data-src="resources/static/images/etc/house.PNG">주택종류별</option>
					<option value="cause"
						data-src="resources/static/images/etc/cause.PNG">원인별</option>
					<option value="careless"
						data-src="resources/static/images/etc/careless.PNG">부주의
						유형별</option>
				</optgroup>
			</select>
			<div id="change_img" align="center"></div>
		</form>
	</div>
</div>
<br>
<%@ include file="/WEB-INF/views/footer.jsp"%>