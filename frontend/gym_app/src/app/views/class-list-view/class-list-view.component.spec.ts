import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClassListViewComponent } from './class-list-view.component';

describe('ClassListViewComponent', () => {
  let component: ClassListViewComponent;
  let fixture: ComponentFixture<ClassListViewComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ClassListViewComponent]
    });
    fixture = TestBed.createComponent(ClassListViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
