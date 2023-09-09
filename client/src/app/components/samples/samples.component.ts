import {
  Component,
  ElementRef,
  EventEmitter,
  OnInit,
  Output,
  ViewChild,
} from '@angular/core';

@Component({
  selector: 'app-samples',
  templateUrl: './samples.component.html',
  styleUrls: ['./samples.component.css'],
})
export class SamplesComponent implements OnInit {
  constructor() {}

  ngOnInit(): void {}

  ngAfterViewInit(): void {
  }
  samplesData = [
    {
      image: '../../../assets/Images/image_pred.png',
      alt: 'sample-image-1',
      content: 'Mean Absolute Percentage Error : 10.660%',
      for: 'item-1',
      id: 'sample-1',
    },
    {
      image: '../../../assets/Images/chatbot.png',
      alt: 'sample-image-2',
      content: 'ChatBot',
      for: 'item-2',
      id: 'sample-2',
    },
    {
      image: '../../../assets/Images/vis_pie.png',
      alt: 'sample-image-3',
      content: 'Visualize',
      for: 'item-3',
      id: 'sample-3',
    },
  ];
}
