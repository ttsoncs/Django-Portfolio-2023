import { annotate, annotationGroup } from 'https://unpkg.com/rough-notation?module'

const e1 = document.querySelector('#n1')
const e2 = document.querySelector('#n2')
const e3 = document.querySelector('#n3')
const e4 = document.querySelector('#n4')

const a1 = annotate(e1, { type: 'underline', color: '#FF218C', strokeWidth: '1.5' })
const a2 = annotate(e2, { type: 'underline', color: '#FFD800', strokeWidth: '1.5' })
const a3 = annotate(e3, { type: 'underline', color: '#21B1FF', strokeWidth: '1.5' })
const a4 = annotate(e4, { type: 'underline', color: '#9c9c9c', strokeWidth: '1', iterations: 1, animate: false, padding: -5 }) 

const ag = annotationGroup([a1, a2, a3]);
ag.show();

a4.show();

