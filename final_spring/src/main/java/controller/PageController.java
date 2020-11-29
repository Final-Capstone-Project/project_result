package controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class PageController {

	@RequestMapping(value = "/index", method = RequestMethod.GET)
	public void index() {

	}

	@RequestMapping(value = "/camera", method = RequestMethod.GET)
	public void camera() {

	}

	@RequestMapping(value = "/fireNews", method = RequestMethod.GET)
	public void fireNews() {

	}

	@RequestMapping(value = "/fireStatus", method = RequestMethod.GET)
	public void fireStatus() {

	}

	@RequestMapping(value = "/loginForm", method = RequestMethod.GET)
	public void loginForm() {

	}

	@RequestMapping(value = "/registerForm", method = RequestMethod.GET)
	public void registerForm() {

	}
}