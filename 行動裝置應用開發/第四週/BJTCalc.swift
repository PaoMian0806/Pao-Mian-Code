//
//  ViewController.swift
//  DivBias093213_test
//
//  Created by user on 2022/11/2.
//  Copyright © 2022 rain. All rights reserved.
//
 
import UIKit
 
class ViewController: UIViewController {
 
    
    
    @IBOutlet weak var r1Value: UILabel!
    @IBOutlet weak var r2Value: UILabel!
    @IBOutlet weak var rcValue: UILabel!
    @IBOutlet weak var reValue: UILabel!
    @IBOutlet weak var r1Slider: UISlider!
    @IBOutlet weak var r2Slider: UISlider!
    @IBOutlet weak var rcSlider: UISlider!
    @IBOutlet weak var reSlider: UISlider!
    
    @IBOutlet weak var icValue: UITextField!
    @IBOutlet weak var vecValue: UITextField!
    
    @IBAction func r1Changed(_ sender: Any) {
        r1Value.text = String(format: "%.1fk", r1Slider.value)
        
        let beta = 99.0
        let veb = 0.7
        
        let r1 = r1Slider.value
        let r2 = r2Slider.value
        let rc = rcSlider.value
        let re = reSlider.value
        
        let rbb = (r1 * r2) / (r1 + r2)
        let vbb = (12.0) * ((r2) / (r1 + r2))
        let ib:Double = (vbb - veb) / (rbb + ((1 + beta) * re))
        let ic:Double = (vbb - veb) / ((rbb / beta) + re)
        let vec = (12.0) - ((beta * ib) * rc) - (((1 + beta) * ib) * re)
        
        if vec <= (-12.0) {
            vecValue.text = String(format: "-12.0 V")
            icValue.text = String(format: "0 mA")
        }
        else {
            vecValue.text = String(
                format: "%.1f V", vec)
            icValue.text = String(format: "%.1f mA", ic)
        }
        
        
        
        /* let height = Double(textHeight.text!)!
        let weight = Double(textWeight.text!)!
        let bmi = weight / (height / 100) / (height / 100)*/
    }
    @IBAction func r2Changed(_ sender: Any) {
        r2Value.text = String(format: "%.1fk", r2Slider.value)
        
        let beta = 99.0
        let veb = 0.7
        let r1 = r1Slider.value
        let r2 = r2Slider.value
        let rc = rcSlider.value
        let re = reSlider.value
        
        let rbb = (r1 * r2) / (r1 + r2)
        let vbb = (12.0) * ((r2) / (r1 + r2))
        let ib:Double = (vbb - veb) / (rbb + ((1 + beta) * re))
        let ic:Double = (vbb - veb) / ((rbb / beta) + re)
        let vec = (12.0) - ((beta * ib) * rc) - (((1 + beta) * ib) * re)
        
        if vec <= (-12.0) {
            vecValue.text = String(format: "-12.0 V")
            icValue.text = String(format: "0 mA")
        }
        else {
            vecValue.text = String(format: "%.1f V", vec)
            icValue.text = String(format: "%.1f mA", ic)
        }
        
    }
    @IBAction func rcChanged(_ sender: Any) {
        rcValue.text = String(format: "%.1fk", rcSlider.value)
        
        let beta = 99.0
        let veb = 0.7
        let r1 = r1Slider.value
        let r2 = r2Slider.value
        let rc = rcSlider.value
        let re = reSlider.value
        
        let rbb = (r1 * r2) / (r1 + r2)
        let vbb = (12.0) * ((r2) / (r1 + r2))
        let ib:Double = (vbb - veb) / (rbb + ((1 + beta) * re))
        let ic:Double = (vbb - veb) / ((rbb / beta) + re)
        let vec = (12.0) - ((beta * ib) * rc) - (((1 + beta) * ib) * re)
        
        if vec <= (-12.0) {
            vecValue.text = String(format: "-12.0 V")
            icValue.text = String(format: "0 mA")
        }
        else {
            vecValue.text = String(format: "%.1f V", vec)
            icValue.text = String(format: "%.1f mA", ic)
        }
        
    }
    @IBAction func reChanged(_ sender: Any) {
        reValue.text = String(format: "%.1fk", reSlider.value)
        
        let beta = 99.0
        let veb = 0.7
        let r1 = r1Slider.value
        let r2 = r2Slider.value
        let rc = rcSlider.value
        let re = reSlider.value
        
        let rbb = (r1 * r2) / (r1 + r2)
        let vbb = (12.0) * ((r2) / (r1 + r2))
        let ib:Double = (vbb - veb) / (rbb + ((1 + beta) * re))
        let ic:Double = (vbb - veb) / ((rbb / beta) + re)
        let vec = (12.0) - ((beta * ib) * rc) - (((1 + beta) * ib) * re)
        
        if vec <= (-12.0) {
            vecValue.text = String(format: "-12.0 V")
            icValue.text = String(format: "0 mA")
        }
        else {
            vecValue.text = String(format: "%.1f V", vec)
            icValue.text = String(format: "%.1f mA", ic)
        }
        
        
    }
    
    
    
    
    
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
