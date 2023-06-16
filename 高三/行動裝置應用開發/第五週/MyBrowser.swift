//
//  ViewController.swift
//  MyBrowser
//
//  Created by user on 2022/11/16.
//  Copyright © 2022 chaoan. All rights reserved.
//

import UIKit
import WebKit

class ViewController: UIViewController {

    @IBOutlet weak var myWebView: WKWebView!
    @IBOutlet weak var urlText: UITextField!
    
    @IBAction func buttonTouched(_ sender: Any) {
        if let urlStr = urlText.text,
            let url = URL(string: urlStr)
        {
            let request = URLRequest(url: url)
            myWebView.load(request)
        }
        
        /*
         Method 2.
         
         guard let urlStr = urlText.text,
            let url = URL(string: urlStr)
         else {
            return
         }
         let request = URLRequest(url: url)
         myWebView.load(request)
         */
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


}

