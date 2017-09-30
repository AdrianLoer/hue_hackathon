//
//  ViewController.swift
//  hue_app
//
//  Created by Adrian Loer on 9/30/17.
//  Copyright © 2017 Adrian Loer. All rights reserved.
//

import UIKit
import Starscream

    class ViewController: UIViewController, FrameExtractorDelegate {

    
    var frameExtractor: FrameExtractor!
    
    @IBOutlet weak var imageView: UIImageView!
        
//    var socket = WebSocket(url: URL(string: "ws://10.1.228.146:80/ws")!)
    var socket = WebSocket(url: URL(string: "ws://192.168.0.100:80/ws")!)
        
        
        
    override func viewDidLoad() {
        super.viewDidLoad()
        frameExtractor = FrameExtractor()
        frameExtractor.delegate = self
        socket.delegate = self
        socket.connect()
    }
        
    func captured(image: UIImage) {
        let jpegCompressionQuality: CGFloat = 0.1 // Set this to whatever suits your purpose
        if let base64String = UIImageJPEGRepresentation(image, jpegCompressionQuality)?.base64EncodedString() {
            socket.write(string: base64String)
        }
        imageView.image = image
    }
}

// MARK: - WebSocketDelegate
extension ViewController : WebSocketDelegate {
    func websocketDidConnect(socket: WebSocketClient) {
        print("connected")
        socket.write(string: "test")
    }

    func websocketDidDisconnect(socket: WebSocketClient, error: Error?) {

    }

    func websocketDidReceiveMessage(socket: WebSocketClient, text: String) {

    }

    func websocketDidReceiveData(socket: WebSocketClient, data: Data) {

    }

    func websocketDidConnect(_ socket: Starscream.WebSocket) {

    }

    func websocketDidDisconnect(_ socket: Starscream.WebSocket, error: Error?) {

    }

    func websocketDidReceiveMessage(_ socket: Starscream.WebSocket, text: String) {

    }

    func websocketDidReceiveData(_ socket: Starscream.WebSocket, data: Data) {

    }
}

