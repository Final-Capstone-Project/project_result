package controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import biz.board.service.BoardService;
import biz.board.vo.BoardVO;

public class BoardController {

	@Autowired
	BoardService service;

	@RequestMapping("/board/main.do")
	public String gotoMain() {
		return "index";
	}
	
	@RequestMapping("/board/list.do")
	public ModelAndView list() {
		ModelAndView mav = new ModelAndView();
		mav.addObject("boardlists", service.getBoardList());
		mav.setViewName("/board/board_list");
		return mav;
	}
	
	@RequestMapping("/board/view.do")
	public ModelAndView view(@RequestParam("board_id") int board_id) {
		ModelAndView mav = new ModelAndView();
		mav.addObject("boardlists", service.getBoard(board_id));
		mav.setViewName("/board/board_view");
		return mav;
	}
	
	@RequestMapping(value = "/board/add.do", method = RequestMethod.POST)
	public String addBoard(BoardVO vo, HttpServletRequest req) throws Exception {
		System.out.println(vo);
		service.addBoard(vo);
		return "redirect:/board/list.do";
	}
	
	@RequestMapping("/board/remove.do")
	public ModelAndView remove(int board_id) {
		service.removeBoard(board_id);
		ModelAndView mav = new ModelAndView();
		mav.addObject("removecomplete", "removecomplete");
		mav.setViewName("/board/board_list");
		return mav;
	}
	
	// modify, update, search 추가
}
