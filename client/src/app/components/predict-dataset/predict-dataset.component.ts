import {
  Component,
  ElementRef,
  EventEmitter,
  OnInit,
  Output,
  ViewChild,
} from '@angular/core';
import { GetData } from 'src/app/models/GetData';
import { FlaskapiService } from 'src/app/flaskapi.service';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { NgxSpinnerService } from 'ngx-spinner';

@Component({
  selector: 'app-predict-dataset',
  templateUrl: './predict-dataset.component.html',
  styleUrls: ['./predict-dataset.component.css'],
  providers: [FlaskapiService],
})
export class PredictDatasetComponent implements OnInit {
  public predictDatasetSubscription: Subscription;
  predictDatasetLink: ElementRef;
  savedPredictionsLink: ElementRef;
  navbarContainer: ElementRef;
  navBrand: ElementRef;
  home: ElementRef;
  samplesLink: ElementRef;
  moreInfoLink: ElementRef;
  predictForm: FormGroup;
  showForm:boolean=false;
  public columnName: Subscription;
  public columnArray:any;
  columnCome:boolean =false;
  submitted: boolean = false;
  formData: any;
  public file: any;

  constructor(
    private flaskApiService: FlaskapiService,
    private router: Router,
    private formBuilder: FormBuilder,
    private spinner: NgxSpinnerService
  ) {}

  ngOnInit(): void {
    this.predictForm = this.formBuilder.group({
      file: ['', Validators.required],
      title: ['', [Validators.required, Validators.maxLength(25)]],
      predictColumn: ['', Validators.required],
      periodicity: ['', Validators.required],
      numericalValue: ['', [Validators.required, Validators.min(1)]],
    });
  }

  ngAfterViewInit(): void {
    this.savedPredictionsLink.nativeElement.setAttribute(
      'style',
      'color: none !important'
    );
    this.moreInfoLink.nativeElement.setAttribute(
      'style',
      'color: none !important'
    );
    this.predictDatasetLink.nativeElement.setAttribute(
      'style',
      'color: none !important'
    );
    this.navbarContainer.nativeElement.classList.add('bg-dark');
    this.navBrand.nativeElement.setAttribute(
      'style',
      'color: none !important'
    );

    this.home.nativeElement.setAttribute(
      'style',
      'color: none !important'
    );
  }
  ngOnDestroy() {
    if (this.predictDatasetSubscription) {
      this.predictDatasetSubscription.unsubscribe();
    }
  }
  getColumnNames(){
    this.spinner.show('signIn');
    this.columnName=this.flaskApiService
    .getColumnName(this.file)
    .subscribe({
      next: (response) => {
        console.log('bshfa');
        this.columnArray=response;
        console.log(this.columnArray);
        this.showForm=true;
        this.spinner.hide('signIn');
      },
      error: (error) => {
        this.spinner.hide('signIn');
      },
  })
}

  getFile(event: any) {
    this.file = event.target.files[0];
    this.getColumnNames();
    
  }

  submitData() {
    this.submitted = true;
    if (this.predictForm.valid) {
      this.spinner.show();
      this.formData = {
        title: this.predictForm.controls['title'].value,
        predictColumn: this.predictForm.controls['predictColumn'].value,
        periodicity: this.predictForm.controls['periodicity'].value,
        numericalValue: this.predictForm.controls['numericalValue'].value,
      };
      this.predictDatasetSubscription = this.flaskApiService
        .postData(this.formData, this.file, localStorage.getItem('email'))
        .subscribe((response) => {
          localStorage.setItem('show', 'true');
          this.router.navigate(['/prediction-result']);
          this.submitted = false;
        });
    }
  }
}
