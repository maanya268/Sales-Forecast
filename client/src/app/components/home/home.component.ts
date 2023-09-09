import { Component, ElementRef, HostListener, OnInit } from '@angular/core';
import { Router } from '@angular/router';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
})
export class HomeComponent implements OnInit {
  homeLink: ElementRef;
  header: ElementRef;

  current: any;
  logInAlert: boolean;
  constructor(private router: Router) {}

  ngOnInit(): void {
    if (localStorage.getItem('email')) {
      this.logInAlert = false;
    } else {
      this.current = 'Please login to start predicting!';
      this.logInAlert = true;
    }
  }

  ngAfterViewInit(): void { 
    this.homeLink.nativeElement.addEventListener('click', () => {
      this.header.nativeElement.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
        inline: 'nearest',
      });
    });
  }
}
