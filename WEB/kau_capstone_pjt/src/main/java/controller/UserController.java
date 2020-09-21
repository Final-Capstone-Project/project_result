package controller;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import biz.user.service.UserService;
import biz.user.vo.UserVO;

@Controller
public class UserController {
	
	@Autowired
	UserService service;
	
	// 로그인화면 입장
	@RequestMapping(value = "/user/login.do", method = RequestMethod.GET)
	public ModelAndView login() {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("user/user_login");
		return mav;
	}
	
	// 로그인
	@RequestMapping(value = "/user/login.do", method = RequestMethod.POST)
	public ModelAndView login(@RequestParam("user_id") String id, @RequestParam("pw") String pw,
			HttpServletRequest req) {
		ModelAndView mav = new ModelAndView();
		UserVO vo = service.login(id, pw);
		if (vo != null) { // 로그인 성공
			req.getSession().setAttribute("user", vo);
			req.getSession().setAttribute("login", vo);
			mav.setViewName("redirect:http://localhost:9000/my/index.jsp");
		} else { // 로그인 실패
			mav.setViewName("user/user_login");
		}
		return mav;
	}
	
	// 로그아웃
	@RequestMapping("/logout.do")
	public ModelAndView logout(HttpServletRequest req) {
		ModelAndView mav = new ModelAndView();
		req.getSession().invalidate();
		mav.setViewName("redirect:http://localhost:9000/my/index.jsp");
		return mav;
	}
	
	// 회원가입 페이지 입장
	@RequestMapping(value = "/user/add.do", method = RequestMethod.GET)
	public ModelAndView addUser() {
		ModelAndView mav = new ModelAndView();
		mav.setViewName("user/user_signup");
		return mav;
	}
	
	// 회원가입
	@RequestMapping(value = "/user/add.do", method = RequestMethod.POST)
	public ModelAndView addUser(UserVO vo, HttpServletRequest req) throws Exception {
		// 동적 바인딩 하기 위해서 setter 내의 변수 이름과 입력값 넘겨줄 <form>태그 input 이름 맞춰줄 것
		ModelAndView mav = new ModelAndView();
		mav.setViewName("redirect:/user/login.do");
		service.addUser(vo);
		return mav;
	}
	
	// 회원탈퇴
	@RequestMapping("/user/remove.do")
	public ModelAndView userRemove(HttpSession session) {
		ModelAndView mav = new ModelAndView();
		UserVO vo = (UserVO) session.getAttribute("user");
		service.removeUser(vo.getUser_id());
		session.invalidate();

		mav.setViewName("redirect:http://localhost:9000/index.jsp");
		return mav;
	}
	
	// 수정 페이지로 이동
	@RequestMapping("/user/modify.do")
	public ModelAndView userModify(HttpSession session) {
		ModelAndView mav = new ModelAndView();
		UserVO vo = (UserVO) session.getAttribute("user");
		mav.addObject("user", service.getUser(vo.getUser_id()));
		mav.setViewName("/user/user_modify");
		return mav;
	}
	
	// 정보 수정 실행
	@RequestMapping("/user/update.do")
	// 자동적으로 Model에 바인딩되는 커맨드객체의 이름을 명시적으로 지정해준것
	public String userUpdate(@ModelAttribute("user") UserVO vo) {
		service.updateUser(vo);
		return "/user/user_view";
	}
	
}
